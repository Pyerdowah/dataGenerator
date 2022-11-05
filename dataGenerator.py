import csv
import datetime
import random
import time

import numpy as np
from faker import Faker

from model.CsvData import CsvData
from model.Employee import Employee
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
        age = fake.random.randint(18, 60)
        employees.append(Employee(age,
                                  fake.random.randint(0, age - 18),
                                  round(fake.random.uniform(4000.0, 10000.0), 2),
                                  np.random.choice(agencies),
                                  fake.first_name(), fake.last_name()))


def generateHotels(howMany):
    faker1 = Faker("en_UK")
    for i in range(howMany):
        hotels.append(Hotel(fake.random.randint(2, 5),
                            "Hotel " + faker1.first_name(),
                            faker1.address(),
                            fake.country(),
                            fake.paragraph()))


def generateFood():
    for i in range(len(hotels)):
        for j in range(len(kindsOfFood)):
            food.append(Food(i, j, kindsOfFood[j]))


def generateRooms():
    for i in range(len(hotels)):
        for j in range(fake.random.randint(4, 100)):
            rooms.append(Room(i, j, fake.random.randint(2, 6)))


def calculateMaxNumberOfGuests(id):
    counter = 0
    for room in rooms:
        if room.hotelId == id:
            counter += room.getNumberOfSeatsInTheRoom()
    return counter


def generateStays(start, end, howMany):
    for i in range(howMany):
        dateOfContract = random_day_date(start, end, random.random())
        startDate = random_day_date(dateOfContract, end, random.random())
        endDate = datetime.datetime.strftime(
            datetime.datetime.strptime(startDate, '%d-%m-%Y') + datetime.timedelta(fake.random.randint(4, 15)),
            '%d-%m-%Y')
        hotel = np.random.choice(hotels)
        stays.append(Stay(startDate,
                          endDate,
                          fake.random.randint(10, calculateMaxNumberOfGuests(hotel.getHotelId())),
                          hotel.getHotelId(),
                          round(fake.random.uniform(10000.0, 15000.0), 2),
                          dateOfContract,
                          np.random.choice(employees).getEmployeeId()))


def generateInsurances(start, end, howMany):
    for i in range(howMany):
        insurances.append(Insurance(np.random.choice(kindsOfInsurance),
                                    round(fake.random.uniform(10000.0, 15000.0), 2),
                                    random_day_date(start, end, random.random()),
                                    np.random.choice(employees).getEmployeeId()))


hotelTransport = {}


def generateTransports(start, end, id):
    for k in range(id, len(stays)):
        numberOfSeatsAvailable = stays[k].getNumberOfSeats()
        cities = []
        for city in citiesOfDeparture:
            cities.append(city)
        for i in range(fake.random.randint(1, len(citiesOfDeparture))):
            cityOfDeparture = np.random.choice(cities)
            for city in cities:
                if city == cityOfDeparture:
                    cities.remove(city)
            if numberOfSeatsAvailable > 1:
                numberOfSeatsTaken = np.random.randint(1, numberOfSeatsAvailable)
            else:
                numberOfSeatsTaken = 1
            numberOfSeatsAvailable -= numberOfSeatsTaken
            if numberOfSeatsAvailable <= 0:
                numberOfSeatsAvailable = numberOfSeatsTaken
            startdateStart = datetime.datetime.strptime(stays[k].getStartDate(), '%d-%m-%Y')
            startdateEnd = datetime.datetime.strptime(stays[k].getStartDate(), '%d-%m-%Y').replace(hour=23, minute=59)
            startdateStart = datetime.datetime.strftime(startdateStart, '%d-%m-%Y %H:%M')
            startdateEnd = datetime.datetime.strftime(startdateEnd, '%d-%m-%Y %H:%M')
            startDate = random_hour_date(startdateStart, startdateEnd, random.random())
            enddateStart = datetime.datetime.strptime(stays[k].getEndDate(), '%d-%m-%Y')
            enddateEnd = datetime.datetime.strptime(stays[k].getEndDate(), '%d-%m-%Y').replace(hour=23, minute=59)
            enddateStart = datetime.datetime.strftime(enddateStart, '%d-%m-%Y %H:%M')
            enddateEnd = datetime.datetime.strftime(enddateEnd, '%d-%m-%Y %H:%M')
            endDate = random_hour_date(enddateStart, enddateEnd, random.random())
            transports.append(Transport(numberOfSeatsTaken,
                                        cityOfDeparture,
                                        hotels[stays[k].hotelId].country,
                                        startDate,
                                        endDate,
                                        np.random.choice(meansOfTransport),
                                        round(fake.random.uniform(10000.0, 20000.0), 2),
                                        random_day_date(start, stays[k].getStartDate(), random.random()),
                                        np.random.choice(employees).getEmployeeId(),
                                        np.random.choice(namesOfTansportCompanies)))
            hotelTransport[len(transports) - 1] = stays[k]
            if numberOfSeatsAvailable == numberOfSeatsTaken:
                break


y = 2021
seasons = {'Lato': (datetime.datetime(y, 6, 21), datetime.datetime(y, 9, 22)),
           'Jesień': (datetime.datetime(y, 9, 23), datetime.datetime(y, 12, 20)),
           'Wiosna': (datetime.datetime(y, 3, 21), datetime.datetime(y, 6, 20))}


def get_season(date):
    date = datetime.datetime.strptime(date, '%d-%m-%Y')
    for season, (season_start, season_end) in seasons.items():
        if season_start <= date <= season_end:
            return season
    else:
        return 'Zima'


def generateOffers(start, end, howMany, id, x):
    for i in range(id, len(transports)):
        transport = transports[i]
        stay = hotelTransport[i]
        numberOfSeats = min(stay.getNumberOfSeats(), transport.getNumberOfSeats())
        insurance = np.random.choice(insurances)
        if x == 1 and insurances.index(insurance) > howMany:
            insurance.setDateOfContract(random_day_date(start, stay.getStartDate(), random.random()))
        elif x == 0:
            insurance.setDateOfContract(random_day_date(start, stay.getStartDate(), random.random()))
        offers.append(Offer(stay.stayId, transport.transportId,
                            np.random.choice(employees).getEmployeeId(),
                            insurance.getInsuranceId(),
                            numberOfSeats,
                            round((transport.getPrice() + insurance.getPrice() + stay.getPrice()) / numberOfSeats, 2),
                            stay.getStartDate(),
                            stay.getEndDate(),
                            get_season(stay.getStartDate())))


rows = []
kindsOfInsuranceForClients = ["Podstawowe", "Rozszerzone", "Premium"]


def generateCsv(id):
    for i in range(id, len(offers)):
        availableSeats = offers[i].getNumberOfSeats()
        costPerPersonForCompany = offers[i].getCost()
        marge = 1.5
        for j in range(fake.random.randint(0, availableSeats)):
            if availableSeats > 0:
                numberOfBuyedSeats = fake.random.randint(1, availableSeats)
                additionalCost = round(fake.random.uniform(500.0, 1000.0), 2)
                rows.append(CsvData(fake.last_name(),
                                    i,
                                    numberOfBuyedSeats,
                                    np.random.choice(kindsOfInsuranceForClients),
                                    np.random.choice(kindsOfFood),
                                    round(
                                        costPerPersonForCompany * numberOfBuyedSeats * marge + additionalCost * numberOfBuyedSeats,
                                        2)))
                availableSeats -= numberOfBuyedSeats


howMany = 5
t1periodStart = "1-1-2021"
t1periodEnd = "31-12-2021"
generateEmployees(howMany)
generateHotels(howMany)
generateFood()
generateRooms()
generateStays(t1periodStart, t1periodEnd, howMany)
generateInsurances(t1periodStart, t1periodEnd, howMany)
generateTransports(t1periodStart, t1periodEnd, 0)
generateOffers(t1periodStart, t1periodEnd, howMany, 0, 0)
generateCsv(0)


def loadDataToFile(fileName, list):
    with open(fileName, "w", encoding="UTF-16") as f:
        for i in list:
            f.write(str(i))
            f.write('\n')


loadDataToFile("employee_t1.bulk", employees)
loadDataToFile("insurances_t1.bulk", insurances)
loadDataToFile("transports_t1.bulk", transports)
loadDataToFile("hotels_t1.bulk", hotels)
loadDataToFile("food_t1.bulk", food)
loadDataToFile("rooms_t1.bulk", rooms)
loadDataToFile("stays_t1.bulk", stays)
loadDataToFile("offers_t1.bulk", offers)

with open('fake_data_t1.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    csv_fake_data = csv.writer(csvfile)
    for i in rows:
        row = i.generateTuple()
        csv_fake_data.writerow(row)

t2periodStart = "1-1-2022"
t2periodEnd = "31-12-2022"

for employee in employees:
    if employee.age >= 60:
        employees.remove(employee)
    else:
        employee.age += 1
        employee.lengthOfWork += 1

id = len(transports)
howManyStays = len(stays)
for i in range(fake.random.randint(0, howMany)):
    age = fake.random.randint(18, 60)
    employees.append(Employee(age,
                              0,
                              round(fake.random.uniform(4000.0, 10000.0), 2),
                              np.random.choice(agencies),
                              fake.first_name(), fake.last_name()))

generateStays(t2periodStart, t2periodEnd, howMany)
generateInsurances(t2periodStart, t2periodEnd, howMany)
generateTransports(t2periodStart, t2periodEnd, howManyStays)
generateOffers(t2periodStart, t2periodEnd, howMany, id, 1)
generateCsv(id)

loadDataToFile("employee_t2.bulk", employees)
loadDataToFile("insurances_t2.bulk", insurances)
loadDataToFile("transports_t2.bulk", transports)
loadDataToFile("hotels_t2.bulk", hotels)
loadDataToFile("food_t2.bulk", food)
loadDataToFile("rooms_t2.bulk", rooms)
loadDataToFile("stays_t2.bulk", stays)
loadDataToFile("offers_t2.bulk", offers)

with open('fake_data_t2.csv', 'w', newline='', encoding="UTF-8") as csvfile:
    csv_fake_data = csv.writer(csvfile)
    for i in rows:
        row = i.generateTuple()
        csv_fake_data.writerow(row)
