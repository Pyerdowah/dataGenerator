class Food:
    def __init__(self, hotelId, kind):
        self.hotelId = hotelId
        self.kind = kind

    def __str__(self):
        return str(self.hotelId) + "|" + str(self.kind)

