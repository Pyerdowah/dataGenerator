class Food:
    def __init__(self, foodId, hotelId, kind):
        self.foodId = foodId
        self.hotelId = hotelId
        self.kind = kind

    def __str__(self):
        return str(self.foodId) + " " + str(self.hotelId) + " " + str(self.kind)

