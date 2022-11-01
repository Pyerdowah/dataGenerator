class CsvData:
    def __init__(self, buyerLastname, offerId, numberOfBuyedSeats, insuranceKind, foodKind, cost):
        self.buyerLastname = buyerLastname
        self.offerId = offerId
        self.numberOfBuyedSeats = numberOfBuyedSeats
        self.insuranceKind = insuranceKind
        self.foodKind = foodKind
        self.cost = cost

    def generateTuple(self):
        return (self.buyerLastname, self.offerId, self.numberOfBuyedSeats, self.insuranceKind, self.foodKind, self.cost)