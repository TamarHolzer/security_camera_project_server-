class Point:
    def __init__(self, room_id, x, y, point_id=-1):
        self.room_id = room_id
        self.x = x
        self.y = y
        self.point_id = point_id

    def __str__(self):
        return f"Point(ID: {self.point_id}, room ID: {self.room_id}, x position: {self.x}, y position: {self.y})"
