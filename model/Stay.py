import itertools


class Stay:
    stayId = itertools.count()

    def __init__(self, dateOfStart, dateOfEnd, numberOfSeats, hotelId, price, dateOfContract,
                 employeeIdWhoContracted):
        self.stayId = next(Stay.stayId)
        self.dateOfStart = dateOfStart
        self.dateOfEnd = dateOfEnd
        self.numberOfSeats = numberOfSeats
        self.hotelId = hotelId
        self.price = price
        self.dateOfContract = dateOfContract
        self.employeeWhoContracted = employeeIdWhoContracted

    def __str__(self):
        return str(self.stayId) + "|" + str(self.dateOfStart) + "|" + str(self.dateOfEnd) + "|" + str(
            self.numberOfSeats) \
               + "|" + str(self.hotelId) + "|" + str(self.price) + "|" + str(self.dateOfContract) + "|" + str(
            self.employeeWhoContracted)

    def getNumberOfSeats(self):
        return self.numberOfSeats

    def getPrice(self):
        return self.price

    def getStartDate(self):
        return self.dateOfStart

    def getEndDate(self):
        return self.dateOfEnd
