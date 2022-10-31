import random
import time
import datetime

from faker import Faker
from model.Employee import Employee
import numpy as np

from model.Hotel import Hotel
from model.Insurance import Insurance
from model.Transport import Transport

fake = Faker("pl_PL")

employees = []
agencies = ["Filia 1", "Filia 2", "Filia 3", "Filia 4", "Filia 5"]
insurances = []
kindsOfInsurance = ["Wypoczynkowy", "Sportowy"]
transports = []
meansOfTransport = ["samolot", "autokar"]
namesOfTansportCompanies = ["A", "B", "C", "D", "E"]
citiesOfDeparture = ["Gdańsk", "Rzeszów", "Warszawa", "Olsztyn", "Katowice", "Kielce", "Kraków", "Szczecin", "Bydgoszcz"]
hotels = []

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))


def random_day_date(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y', prop)


def random_hour_date(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y %H:%M', prop)


def generateEmployees(howMany):
    for i in range(howMany):
        employees.append(Employee(i,
                                  fake.random.randint(0, 40),
                                  round(fake.random.uniform(4000.0, 10000.0), 2),
                                  np.random.choice(agencies),
                                  fake.first_name(), fake.last_name()))


def generateInsurances(howMany):
    for i in range(howMany):
        insurances.append(Insurance(i, np.random.choice(kindsOfInsurance),
                                    round(fake.random.uniform(100000.0, 150000.0), 2),
                                    random_day_date("1-1-2021", "31-12-2021", random.random()),
                                    np.random.choice(employees).getEmployeeId()))


def generateTransports(howMany):
    for i in range(howMany):
        dateOfContract = random_hour_date("1-1-2021 00:00", "31-12-2021 23:59", random.random())
        startDate = random_hour_date(dateOfContract, "31-12-2021 23:59", random.random())
        date = datetime.datetime.strptime(startDate, '%d-%m-%Y %H:%M')
        endDate = datetime.datetime.strftime(date + datetime.timedelta(fake.random.randint(4, 15)), '%d-%m-%Y %H:%M')
        transports.append(Transport(i,
                                    np.random.randint(10, 40),
                                    np.random.choice(citiesOfDeparture),
                                    fake.country(),
                                    startDate,
                                    endDate,
                                    np.random.choice(meansOfTransport),
                                    round(fake.random.uniform(100000.0, 200000.0), 2),
                                    dateOfContract,
                                    np.random.choice(employees).getEmployeeId(),
                                    np.random.choice(namesOfTansportCompanies)))


def generateHotels(howMany):
    faker1 = Faker("en_UK")
    for i in range(howMany):
        hotels.append(Hotel(i,
                            fake.random.randint(2, 5),
                            "Hotel " + faker1.first_name(),
                            faker1.address(),
                            np.random.choice(transports).getDestination(),
                            fake.paragraph()))



howMany = 5
generateEmployees(howMany)
generateInsurances(howMany)
generateTransports(howMany)
generateHotels(howMany)
for i in hotels:
    print(i)
