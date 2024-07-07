#import math
import numpy as np
from shapely.geometry import Point, Polygon

# מציאת הקו הישר בהפרשים של חצי
def find_line(x, y):
    def points_between_coordinates(x1, y1, x2, y2):
        # Calculate the distance between the two points
        distance_x = abs(x2 - x1)
        distance_y = abs(y2 - y1)


        # Determine the number of points to interpolate along the line
        num_points = int(max(distance_x, distance_y) * 2) + 1

        # Generate the coordinates by linearly interpolating between the start and end points
        coordinates = []
        for i in range(num_points):
            t = i / (num_points - 1)
            new_x = x1 + t * (x2 - x1)
            new_y = y1 + t * (y2 - y1)
            coordinates.append((new_x, new_y))

        return coordinates

    x1, y1 = x[0], x[1]
    x2, y2 = y[0], y[1]

    result = points_between_coordinates(x1, y1, x2, y2)
    #print("Points between ({}, {}) and ({}, {}) with a difference of 0.5:".format(x1, y1, x2, y2))
    #print(result)

    # show_line(result)
    return result

#מציאת מסגרת החדר- מיקומים אפשריים למיקום מצלמות אבטחה
def find_room_frame(allCordinated):
    walls = []
    j = 0

    for i in allCordinated:
        if (j < (len(allCordinated) - 1)):
            walls.append(find_line(allCordinated[j], allCordinated[j + 1]))
        else:
            walls.append(find_line(allCordinated[j], allCordinated[0]))
        j += 1
    # polygon.print_polygon(allCordinated)
    return walls

#מציאת הנקודות לכיסוי בתוך החדר
def find_room_targets(cordinates_of_room):

    def generate_grid(polygon, num_points):
        minx, miny, maxx, maxy = polygon.bounds
        x = np.linspace(minx, maxx, num_points)
        y = np.linspace(miny, maxy, num_points)
        grid_points = [Point(x_i, y_i) for x_i in x for y_i in y]
        return grid_points

    def points_inside_polygon(grid_points, polygon):
        return [point for point in grid_points if polygon.contains(point)]

    def points_to_tuples(points):
        return [(float(point.x), float(point.y)) for point in points]

    try:
        # Define polygon
        polygon = Polygon(cordinates_of_room)

        # Generate grid points
        num_points = 15  # Adjust the number of points for different densities
        grid_points = generate_grid(polygon, num_points)

        # Filter points inside the polygon
        inside_points = points_inside_polygon(grid_points, polygon)

        # Convert to list of tuples
        points_tuples = points_to_tuples(inside_points)
        return points_tuples

    except ValueError as e:
        print(f"Error creating polygon: {e}")
        # Handle the error, e.g., return an error response or default value
        return None

