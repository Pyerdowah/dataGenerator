import itertools


class Insurance:
    insuranceId = itertools.count()
    def __init__(self, kind, price, dateOfContract, employeeIdWhoContracted):
        self.insuranceId = next(Insurance.insuranceId)
        self.kind = kind
        self.price = price
        self.dateOfContract = dateOfContract
        self.employeeIdWhoContracted = employeeIdWhoContracted

    def __str__(self):
        return str(self.insuranceId) + "|" + str(self.kind) + "|" + str(self.price) + "|" + str(self.dateOfContract) \
               + "|" + str(self.employeeIdWhoContracted)

    def getInsuranceId(self):
        return self.insuranceId

    def getPrice(self):
        return self.price

    def setDateOfContract(self, dateOfContract):
        self.dateOfContract = dateOfContract
