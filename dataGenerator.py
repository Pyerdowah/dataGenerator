import random
import time
import datetime
import csv

from faker import Faker

from model.CsvData import CsvData
from model.Employee import Employee
import numpy as np

from model.Food import Food
from model.Hotel import Hotel
from model.Insurance import Insurance
from model.Offer import Offer
from model.Room import Room
from model.Stay import Stay
from model.Transport import Transport

fake = Faker("pl_PL")

employees = []
agencies = [1, 2, 3, 4, 5]
insurances = []
kindsOfInsurance = ["Wypoczynkowy", "Sportowy"]
transports = []
meansOfTransport = ["samolot", "autokar"]
namesOfTansportCompanies = ["A", "B", "C", "D", "E"]
citiesOfDeparture = ["Gdańsk", "Rzeszów", "Warszawa", "Olsztyn", "Katowice", "Kielce", "Kraków", "Szczecin",
                     "Bydgoszcz"]
hotels = []
food = []
kindsOfFood = ["BB", "HB", "FB", "AI", "OV", "SC", "PP"]
rooms = []
stays = []
offers = []


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
                                    round(fake.random.uniform(10000.0, 15000.0), 2),
                                    random_day_date("1-1-2021", "31-12-2021", random.random()),
                                    np.random.choice(employees).getEmployeeId()))


def generateTransports(howMany):
    for i in range(howMany):
        dateOfContract = random_hour_date("1-1-2021 00:00", "31-12-2021 23:59", random.random())
        startDate = random_hour_date(dateOfContract, "31-12-2021 23:59", random.random())
        date = datetime.datetime.strptime(startDate, '%d-%m-%Y %H:%M')
        endDate = datetime.datetime.strftime(date + datetime.timedelta(fake.random.randint(4, 15)), '%d-%m-%Y %H:%M')
        transports.append(Transport(i,
                                    np.random.randint(10, 60),
                                    np.random.choice(citiesOfDeparture),
                                    fake.country(),
                                    startDate,
                                    endDate,
                                    np.random.choice(meansOfTransport),
                                    round(fake.random.uniform(10000.0, 20000.0), 2),
                                    datetime.datetime.strptime(dateOfContract, '%d-%m-%Y %H:%M').date(),
                                    np.random.choice(employees).getEmployeeId(),
                                    np.random.choice(namesOfTansportCompanies)))


hotelTransport = {}


def generateHotels(howMany):
    faker1 = Faker("en_UK")
    for i in range(howMany):
        transport = np.random.choice(transports)
        hotels.append(Hotel(i,
                            fake.random.randint(2, 5),
                            "Hotel " + faker1.first_name(),
                            faker1.address(),
                            transport.getDestination(),
                            fake.paragraph()))
        hotelTransport[i] = transport


def generateFood(howMany):
    for i in range(howMany):
        food.append(Food(i, np.random.choice(kindsOfFood)))


def generateRooms():
    for i in range(len(hotels)):
        for j in range(fake.random.randint(4, 100)):
            rooms.append(Room(i, j, fake.random.randint(2, 6)))


def generateStays(howMany):
    for i in range(howMany):
        stays.append(Stay(i,
                          str(datetime.datetime.strftime(
                              datetime.datetime.strptime(hotelTransport[i].getStartDate(), '%d-%m-%Y %H:%M').date(),
                              '%d-%m-%Y')),
                          str(datetime.datetime.strftime(
                              datetime.datetime.strptime(hotelTransport[i].getEndDate(), '%d-%m-%Y %H:%M').date(),
                              '%d-%m-%Y')),
                          fake.random.randint(10, 100),
                          i,
                          round(fake.random.uniform(10000.0, 15000.0), 2),
                          random_day_date("1-1-2021", datetime.datetime.strftime(
                              datetime.datetime.strptime(hotelTransport[i].getStartDate(), '%d-%m-%Y %H:%M').date(),
                              '%d-%m-%Y'), random.random()),
                          np.random.choice(employees).getEmployeeId()))


y = 2021
seasons = {'Lato': (datetime.datetime(y, 6, 21), datetime.datetime(y, 9, 22)),
           'Jesien': (datetime.datetime(y, 9, 23), datetime.datetime(y, 12, 20)),
           'Wiosna': (datetime.datetime(y, 3, 21), datetime.datetime(y, 6, 20))}


def get_season(date):
    date = datetime.datetime.strptime(date, '%d-%m-%Y')
    for season, (season_start, season_end) in seasons.items():
        if season_start <= date <= season_end:
            return season
    else:
        return 'Zima'


def generateOffers(howMany):
    for i in range(howMany):
        numberOfSeats = min(stays[i].getNumberOfSeats(), transports[i].getNumberOfSeats())
        insurance = np.random.choice(insurances)
        transport = transports[i]
        stay = stays[i]
        offers.append(Offer(i, i, hotelTransport[i].getTransportId(),
                            np.random.choice(employees).getEmployeeId(),
                            insurance.getInsuranceId(),
                            numberOfSeats,
                            round((transport.getPrice() + insurance.getPrice() + stay.getPrice()) / numberOfSeats, 2),
                            stay.getStartDate(),
                            stay.getEndDate(),
                            get_season(stay.getStartDate())))


rows = []
kindsOfInsuranceForClients = ["Podstawowe", "Rozszerzone", "Premium"]


def generateCsv():
    for i in range(len(offers)):
        availableSeats = offers[i].getNumberOfSeats()
        costPerPersonForCompany = offers[i].getCost()
        marge = 1.5
        for j in range(fake.random.randint(0, 100)):
            while availableSeats > 0:
                numberOfBuyedSeats = fake.random.randint(1, 10)
                additionalCost = round(fake.random.uniform(1000.0, 3000.0), 2)
                rows.append(CsvData(fake.last_name(),
                                    i,
                                    numberOfBuyedSeats,
                                    np.random.choice(kindsOfInsuranceForClients),
                                    np.random.choice(kindsOfFood),
                                    round(costPerPersonForCompany * numberOfBuyedSeats * marge + additionalCost, 2)))
                availableSeats -= numberOfBuyedSeats


howMany = 5
generateEmployees(howMany)
generateInsurances(howMany)
generateTransports(howMany)
generateHotels(howMany)
generateFood(howMany)
generateRooms()
generateStays(howMany)
generateOffers(howMany)
generateCsv()


with open("eployee_t1.bulk", "w") as f:
    for i in employees:
        f.write(str(i))
        f.write('\n')

with open("insurances_t1.bulk", "w") as f:
    for i in insurances:
        f.write(str(i))
        f.write('\n')


with open("transports_t1.bulk", "w") as f:
    for i in transports:
        f.write(str(i))
        f.write('\n')


with open("hotels_t1.bulk", "w") as f:
    for i in hotels:
        f.write(str(i))
        f.write('\n')


with open("food_t1.bulk", "w") as f:
    for i in food:
        f.write(str(i))
        f.write('\n')


with open("rooms_t1.bulk", "w") as f:
    for i in rooms:
        f.write(str(i))
        f.write('\n')


with open("stays_t1.bulk", "w") as f:
    for i in stays:
        f.write(str(i))
        f.write('\n')


with open("offers_t1.bulk", "w") as f:
    for i in offers:
        f.write(str(i))
        f.write('\n')


with open('fake_data_t1.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    csv_fake_data = csv.writer(csvfile)
    for i in rows:
        row = i.generateTuple()
        csv_fake_data.writerow(row)

