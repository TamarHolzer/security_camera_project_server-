class Apartment:
    def __init__(self, picture_name, of_user_id, apartment_id=-1):
        self.picture_name = picture_name
        self.of_user_id = of_user_id
        self.apartment_id = apartment_id


    def __str__(self):
        return f"Camera(ID: {self.picture_name}, Name: {self.of_user_id}, Vertical Angle: {self.apartment_id})"
