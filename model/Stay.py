class Stay:
    def __init__(self, stayId, dateOfStart, dateOfEnd, numberOfSeats, hotelId, price, dateOfContract, employeeIdWhoContracted):
        self.stayId = stayId
        self.dateOfStart = dateOfStart
        self.dateOfEnd = dateOfEnd
        self.numberOfSeats = numberOfSeats
        self.hotelId = hotelId
        self.price = price
        self.dateOfContract = dateOfContract
        self.employeeWhoContracted = employeeIdWhoContracted

    def __str__(self):
        return str(self.stayId) + " " + str(self.dateOfStart) + " " + str(self.dateOfEnd) + " " + str(self.numberOfSeats)\
               + " " + str(self.hotelId) + " " + str(self.price) + " " + str(self.dateOfContract) + " " + str(self.employeeWhoContracted)
