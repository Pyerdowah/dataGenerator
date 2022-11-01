class Offer:
    def __init__(self, offerId, stayId, transportId, employeeId, insuranceId, numberOfSeats, costPerPerson, dateOfStart, dateOfEnd, season):
        self.offerId = offerId
        self.stayId = stayId
        self.transportId = transportId
        self.employeeId = employeeId
        self.insuranceId = insuranceId
        self.numberOfSeats = numberOfSeats
        self.costPerPerson = costPerPerson
        self.dateOfStart = dateOfStart
        self.dateOfEnd = dateOfEnd
        self.season = season

    def __str__(self):
        return str(self.offerId) + "|" + str(self.stayId) + "|" + str(self.transportId) + "|" + str(self.employeeId) \
               + "|" + str(self.insuranceId) + "|" + str(self.numberOfSeats) + "|" + str(self.costPerPerson)\
               + "|" + str(self.dateOfStart) + "|" + str(self.dateOfEnd) + "|" + str(self.season)

    def getNumberOfSeats(self):
        return self.numberOfSeats

    def getCost(self):
        return self.costPerPerson
