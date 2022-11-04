DROP TABLE OFFER, STAY, ROOM, FOOD, HOTEL, TRANSPORT, INSURANCE, EMPLOYEE

CREATE TABLE EMPLOYEE(
	EMPLOYEEID INT PRIMARY KEY,
	AGE INT,
	LENGTHOFWORK INT,
	SALARY NUMERIC,
	AGENCY INT,
	FIRSTNAME VARCHAR(15),
	LASTNAME VARCHAR(30)
)

CREATE TABLE INSURANCE(
	INSURANCEID INT PRIMARY KEY,
	KIND VARCHAR(30),
	COST NUMERIC,
	DATEOFCONTRACT VARCHAR(20),
	EMPLOYEEID INT
)

CREATE TABLE TRANSPORT(
	TRANSPORTID INT PRIMARY KEY,
	NUMBEROFSEATS INT,
	CITYOFDEPARTURE VARCHAR(30),
	PLACEOFDESTINATION VARCHAR(50),
	DATEOFSTART VARCHAR(20),
	DATEOFEND VARCHAR(20),
	MEANOFTRANSPORT VARCHAR(20),
	COST NUMERIC,
	DATEOFCONTRACT VARCHAR(20),
	EMPLOYEEID INT,
	NAMEOFCOMPANY VARCHAR(30)
)

CREATE TABLE HOTEL(
	HOTELID INT PRIMARY KEY,
	NUMBEROFSTARS INT,
	NAMEOFHOTEL VARCHAR(30),
	ADDRESSOFHOTEL VARCHAR(100),
	COUNTRY VARCHAR(30),
	FACILITIES VARCHAR(1000)
)

CREATE TABLE FOOD(
	HOTELID INT REFERENCES HOTEL,
	FOODID INT,
	KIND CHAR(2),
	PRIMARY KEY(HOTELID, FOODID) 
)

CREATE TABLE ROOM(
	HOTELID INT REFERENCES HOTEL,
	ROOMID INT,
	NUMBEROFSEATSINTHEROOM INT,
	PRIMARY KEY(HOTELID, ROOMID) 
)

CREATE TABLE STAY(
	STAYID INT PRIMARY KEY,
	DATEOFSTART VARCHAR(20),
	DATEOFEND VARCHAR(20), 
	NUMBEROFSEATS INT,
	HOTELID INT REFERENCES HOTEL,
	COST NUMERIC,
	DATEOFCONTRACT VARCHAR(20),
	EMPLOYEEID INT
)

CREATE TABLE OFFER(
	OFFERID INT PRIMARY KEY,
	STAYID INT REFERENCES STAY,
	TRANSPORTID INT REFERENCES TRANSPORT,
	EMPLOYEEID INT REFERENCES EMPLOYEE,
	INSURANCEID INT REFERENCES INSURANCE,
	NUMBEROFSEATS INT,
	COSTPERPERSON NUMERIC,
	DATEOFSTART VARCHAR(20),
	DATEOFEND VARCHAR(20),
	SEASON VARCHAR(10)
)

BULK INSERT dbo.EMPLOYEE FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\employee_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.INSURANCE FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\insurances_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.TRANSPORT FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\transports_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.HOTEL FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\hotels_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.FOOD FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\food_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.ROOM FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\rooms_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.STAY FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\stays_t2.bulk' WITH (FIELDTERMINATOR='|')
BULK INSERT dbo.OFFER FROM 'C:\Users\Paulina\Documents\GitHub\dataGenerator\offers_t2.bulk' WITH (FIELDTERMINATOR='|')

SELECT * FROM OFFER
SELECT * FROM STAY
SELECT * FROM ROOM
SELECT * FROM FOOD
SELECT * FROM HOTEL
SELECT * FROM TRANSPORT
SELECT * FROM INSURANCE
SELECT * FROM EMPLOYEE