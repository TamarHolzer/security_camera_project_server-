import models.Camera as cam
import pypyodbc as odbc

# פונקצית החיבור לDB
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=DESKTOP-V6585A6\SQLEXPRESS;'
    r'DATABASE=SECURITY_CAMERA_PROJECT;'
    r'Trusted_Connection=yes;'
)


def get_all_cameras():
    try:
        conn = odbc.connect(conn_str)
        cursor = conn.cursor()

        # Execute the query to retrieve all camera data
        cursor.execute("SELECT * FROM securityCamera")

        # Fetch all rows from the executed query
        rows = cursor.fetchall()

        # Process the retrieved data
        cameras = []
        for row in rows:
            camera = cam.Camera(row[0], row[1], row[2], row[3], row[4])
            cameras.append(camera)

        # Find the number of cameras
#        num_of_cameras = len(cameras)

        return cameras

    except Exception as e:
        print("Error retrieving camera data:", e)
        return None, 0

#print(get_all_cameras())