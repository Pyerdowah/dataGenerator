class Food:
    def __init__(self, hotelId, foodId, kind):
        self.hotelId = hotelId
        self.foodId = foodId
        self.kind = kind

    def __str__(self):
        return str(self.hotelId) + "|" + str(self.foodId) + "|" + str(self.kind)

