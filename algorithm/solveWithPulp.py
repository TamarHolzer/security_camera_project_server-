import re
import pulp
from algorithm.initilize_v_with_fov import initialize_v_with_fov
import algorithm.constraints.constraintP8 as con8
import algorithm.constraints.constraintP9 as con9
import algorithm.constraints.constraintP10 as con10
from algorithm.constraints.optimizeObject import objective_function

def x_y_extraction(param_string):
    # Define the regex pattern to match numbers inside parentheses
    pattern = r'x_\((\d+),_(\d+),_(\d+),_(\d+),_(\d+)\)'

    # Find all matches
    matches = re.findall(pattern, param_string)

    # Convert matches to a tuple of integers
    if matches:
        indices = tuple(map(int, matches[0]))
        print(indices)

    # Convert matches to a tuple of integers
    if matches:
        indices = tuple(map(int, matches[0]))
        print(indices)  # Output: (100, 2, 3, 0, 0)
        return indices
    else:
        print("No matches found.")

"""
phi- horizontal installation
psi- vertical installation
theta1- horizontal angle of view
theta2- vertical angle of view
"""
#בונה בעיית אופטימיזציה ושולח אותה לPULP
def solve_with_pulp(NC, NhD, NvD, NE, NA, NT, CVR, List_of_possible_camera_locations, list_of_target_positions):
    # Define the problem
    print("open prob")
    prob = pulp.LpProblem("Camera_Optimization", pulp.LpMinimize)

    dictionaryOfTheCountersParam = {
        "NC": NC,
        "NhD": NhD,
        "NvD": NvD,
        "NE": NE,
        "NA": NA,
        "NT": NT,
        "CVR": CVR
    }

    print("params")
    # Assume V is a predefined 6-dimensional array that represents visibility
    v, horizontal_angles_list, vertical_angles_list = initialize_v_with_fov(dictionary_of_the_counters_paramerters=dictionaryOfTheCountersParam, List_of_possible_camera_locations=List_of_possible_camera_locations, list_of_target_psitions=list_of_target_positions)

    # Decision variables
    x = pulp.LpVariable.dicts("x", ((i, j, d, e, t) for i in range(NC) for j in range(NhD)
                                    for d in range(NvD) for e in range(NE) for t in range(NA)), cat='Binary')
    y = pulp.LpVariable.dicts("y", range(NT), cat='Binary')

    # Define the objective function
    objective_function(prob, x, NC, NhD, NvD, NE, NA)
    print("constraints")
    # Add constraints
    con8.inequality_constraint1(prob, x, y, v, NC, NhD, NvD, NE, NA, NT)
    print("con1")
    con9.inequality_constraint2(prob, x, y, v, NC, NT, NhD, NvD, NE, NA)
    print("con2")
    con10.inequality_constraint3(prob, y, NA, NT, CVR)
    print("solving")
    # Solve the problem
    prob.solve()

    # Print the results
    print("Status:", pulp.LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    print("Optimal number of cameras:", pulp.value(prob.objective))


    def extract_indices(var_name):
        pattern = r"x_\((\d+),_(\d+),_(\d+),_(\d+),_(\d+)\)"
        match = re.match(pattern, var_name)
        if match:
            return tuple(map(int, match.groups()))
        return None

    x_indices = []
    for v in prob.variables():
        if v.varValue == 1:
            indices = extract_indices(v.name)

            if indices:
                print(indices[0])
                print(List_of_possible_camera_locations[indices[0]][0])
                r1 = List_of_possible_camera_locations[indices[0]][0]
                r2 = List_of_possible_camera_locations[indices[0]][1]
                r3 = horizontal_angles_list[indices[1]]
                r3 = int(r3)
                r4 = vertical_angles_list[indices[2]]
                r4 = int(r4)
                x_indices.append({"x": r1, "y": r2, "horizontalAngale": r3, "verticalAngale": r4})

    return x_indices
