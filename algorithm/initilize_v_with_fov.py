import numpy as np
from matplotlib.path import Path
from algorithm.computeFov import compute_fov
from functionsDB.camerasFunctionsDB import get_all_cameras


# פונקציה לחישוב הנקודות שנמצאות בתוך הטווח של ה- FOV
def is_point_in_polygon(point, polygon):
    path = Path(polygon)
    return path.contains_point(point)


def check_for_every_horizontal_angle( NhD, NvD, NE, NA, NT,epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations,list_of_target_psitions, v, i):
    for j in range(NhD):  # לכל הזוויות האופקיות
        check_for_every_vertical_angle(NhD, NvD, NE, NA, NT, epsilon, theta1, theta2, vD_list, hD_list, T,
                                       List_of_possible_camera_locations, list_of_target_psitions, v, i, j)


def check_for_every_vertical_angle( NhD, NvD, NE, NA, NT,epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations,list_of_target_psitions, v, i, j):
    for d in range(NvD):  # ולכל הזוויות האנכיות
        check_for_every_heights(NhD, NvD, NE, NA, NT, epsilon, theta1, theta2, vD_list, hD_list, T,
                                      List_of_possible_camera_locations, list_of_target_psitions, v, i, j, d)


def check_for_every_heights(NhD, NvD, NE, NA, NT, epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations, list_of_target_psitions, v, i, j, d):
        for h in range(NE):  # לכל הגבהים של ההתקנה
            check_for_every_kind_of_camera(NhD, NvD, NE, NA, NT, epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations, list_of_target_psitions, v, i, j, d, h)


def check_for_every_kind_of_camera(NhD, NvD, NE, NA, NT, epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations, list_of_target_psitions, v, i, j, d, h):
            for t in range(NA):  # ובודק לכל מצלמה
                fov_vertices = compute_fov(epsilon, theta1, theta2, vD_list[j], hD_list[d], T,
                                           List_of_possible_camera_locations[i][0],
                                           List_of_possible_camera_locations[i][1])  # מחשב את הקורדינאטות של הFOV
                check_for_every_target_position(NT, list_of_target_psitions, v, i, j, d, h, t, fov_vertices)


def check_for_every_target_position(NT, list_of_target_psitions, v, i, j, d, h, t, fov_vertices):
                for k in range(NT):  # עובר על כל הנקודות כיסוי
                    if k >= list_of_target_psitions.__len__():
                        continue
                    elif type(list_of_target_psitions) != list:
                        return None
                    else:
                         v[i, j, d, h, t, k] = is_point_in_polygon(list_of_target_psitions[k], fov_vertices)


def initialize_v_with_fov(dictionary_of_the_counters_paramerters, list_of_target_psitions, List_of_possible_camera_locations):
    cameras_data = get_all_cameras()
    epsilon = 2.5  # height (m)
    theta1 = 80  # default  # horizontal angle of view (degrees) גודל הזווית של מצלמה!!!!
    theta2 = 80  # default # vertical angle of view (degrees) - Adjusted to ensure the angle sum is < 90
    T = 30  # default  # maximum recognition distance (m)

    for camera in cameras_data:
        theta1 = camera.horizontal_angle
        theta2 = camera.vertical_angle
        T = camera.maximum_distance

    # psi = 20  # vertical angle of the camera (degrees)
    # phi = 45  # horizontal angle of the camera (degrees) כיוון ההתקנה של המצלמה!!!!


    """
    # <editor-fold desc="שליפת כל הערכים של כמות המיקומים וכו לתוך משתנים">
    NhD = dictionary_of_the_counters_paramerters['NhD']
    NvD = dictionary_of_the_counters_paramerters['NvD']
    NE = dictionary_of_the_counters_paramerters['NE']
    # </editor-fold>
    """

    NhD = 5
    NvD = 5
    NE = dictionary_of_the_counters_paramerters['NE']
    NA = len(cameras_data)
    NC = dictionary_of_the_counters_paramerters['NC']
    NT = len(list_of_target_psitions)


    #איתחול V באפסים
    v = np.zeros((NC, NhD, NvD, NE, NA, NT))

    hD_list = np.linspace(0, 180-theta1, NhD, dtype='int8')# horizontal angle of the camera (degrees) כיוון ההתקנה של המצלמה!!!!
    vD_list = np.linspace(0, theta2, NvD, dtype='int8') # vertical angle of the camera (degrees)

    print("hD_list", hD_list)
    print("vD_list", vD_list)

    for i in range(NC):  # לכל הנקודות להתקנה
        check_for_every_horizontal_angle(NhD, NvD, NE, NA, NT,epsilon, theta1, theta2, vD_list, hD_list, T, List_of_possible_camera_locations, list_of_target_psitions, v, i)
    print(v)
    return v, hD_list, vD_list



