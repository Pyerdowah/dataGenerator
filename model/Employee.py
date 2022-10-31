class Employee:
    def __init__(self, employeeId, lengthOfWork, salary, agency, firstname, lastname):
        self.employeeId = employeeId
        self.lengthOfWork = lengthOfWork
        self.salary = salary
        self.agency = agency
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return str(self.employeeId) + " " + str(self.lengthOfWork) + " " + str(self.salary) + " " + str(self.agency)\
               + " " + str(self.firstname) + " " + str(self.lastname)

    def getEmployeeId(self):
        return self.employeeId
