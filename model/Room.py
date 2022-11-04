class Room:
    def __init__(self, hotelId, roomId, numberOfSeatsInTheRoom):
        self.hotelId = hotelId
        self.roomId = roomId
        self.numberOfSeatsInTheRoom = numberOfSeatsInTheRoom

    def __str__(self):
        return str(self.hotelId) + "|" + str(self.roomId) + "|" + str(self.numberOfSeatsInTheRoom)

    def getNumberOfSeatsInTheRoom(self):
        return self.numberOfSeatsInTheRoom
