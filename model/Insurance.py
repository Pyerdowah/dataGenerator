class Insurance:
    def __init__(self, insuranceId, kind, price, dateOfContract, employeeIdWhoContracted):
        self.insuranceId = insuranceId
        self.kind = kind
        self.price = price
        self.dateOfContract = dateOfContract
        self.employeeIdWhoContracted = employeeIdWhoContracted

    def __str__(self):
        return str(self.insuranceId) + " " + str(self.kind) + " " + str(self.price) + " " + str(self.dateOfContract)\
               + " " + str(self.employeeIdWhoContracted)