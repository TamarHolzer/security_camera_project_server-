class Room:
    def __init__(self, apartment_id, room_id=-1, RoomName="" ):
        self.apartment_id = apartment_id
        self.room_id = room_id
        self.RoomName = RoomName

    def __str__(self):
        return f"Room(room ID: {self.room_id}, room name: {self.RoomName}, apartment id: {self.apartment_id})"
