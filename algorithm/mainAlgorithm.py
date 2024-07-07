# import math
from algorithm import findPoint, solveWithPulp
# import findPoint
from functionsDB import camerasFunctionsDB
# import solveWithPulp




def main(list_of_tuples_with_the_xy_cordinates=[(20,5),(25,8),(200,120)], heightOfRoomChosenByUser=2.50):
    numOfCameras = camerasFunctionsDB.get_all_cameras()

    NhD = 5 #מספר זוויות התקנה אופקיות
    NvD = 5 #מספר זוויות התקנה אנכיות
    NE = 1 #מספר גבהים
    NA = 1 #סוגי מצלמות
    CVR = 0.9 #כיסוי מינימלי


    # מיקומים אפשריים למצלמות
    point_in_walls = findPoint.find_room_frame(list_of_tuples_with_the_xy_cordinates)
    if point_in_walls == None:
        return None
    else:
        list_of_camera_positions = []
        NC = 0
        for sublist in point_in_walls:
            for coord in sublist:
                list_of_camera_positions.append(coord)
                NC += 1


    # target positions-  עמדות יעד
    target_points_list = findPoint.find_room_targets(list_of_tuples_with_the_xy_cordinates)
    print(f"targets{target_points_list}")

    #מספר עמדות היעד
    NT = len(target_points_list)


    sol = solveWithPulp.solve_with_pulp(NC=NC, NhD=NhD, NvD=NvD, NE=NE, NA=NA, NT=NT, CVR=CVR,  list_of_target_positions=target_points_list, List_of_possible_camera_locations=list_of_camera_positions)
    print(sol)
    return sol




