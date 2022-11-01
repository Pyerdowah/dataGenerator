class Transport:
    def __init__(self, transportId, numberOfSeats, placeOfDeparture, placeOfDestination, dateOfDeparture, dateOfArrival, meanOfTransport, price, dateOfContract, employeeIdWhoContracted, nameOfCompany):
        self.transportId = transportId
        self.numberOfSeats = numberOfSeats
        self.placeOfDeparture = placeOfDeparture
        self.placeOfDestination = placeOfDestination
        self.dateOfDeparture = dateOfDeparture
        self.dateOfArrival = dateOfArrival
        self.meanOfTransport = meanOfTransport
        self.price = price
        self.dateOfContract = dateOfContract
        self.employeeIdWhoContracted = employeeIdWhoContracted
        self.nameOfCompany = nameOfCompany

    def __str__(self):
        return str(self.transportId) + "|" + str(self.numberOfSeats) + "|" + str(self.placeOfDeparture) \
               + "|" + str(self.placeOfDestination) + "|" + str(self.dateOfDeparture) + "|" + str(self.dateOfArrival) \
               + "|" + str(self.meanOfTransport) + "|" + str(self.price) + "|" + str(self.dateOfContract) \
               + "|" + str(self.employeeIdWhoContracted) + "|" + str(self.nameOfCompany)

    def getDestination(self):
        return self.placeOfDestination

    def getStartDate(self):
        return self.dateOfDeparture

    def getTransportId(self):
        return self.transportId

    def getEndDate(self):
        return self.dateOfArrival

    def getNumberOfSeats(self):
        return self.numberOfSeats

    def getPrice(self):
        return self.price
