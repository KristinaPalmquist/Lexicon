-- Create tables
CREATE TABLE City(
	CityId SERIAL NOT NULL Primary Key,
	CityName VARCHAR(50)
);

CREATE TABLE ElevatorType(
	ElevatorTypeId SERIAL NOT NULL Primary Key,
	TypeName VARCHAR(50)
);

CREATE TABLE EmployeeStatus(
	EmployeeStatusId SERIAL NOT NULL Primary Key,
	StatusDescription VARCHAR(50)
);

CREATE TABLE ServiceStatus(
	ServiceStatusId SERIAL NOT NULL Primary Key,
	StatusDescription VARCHAR(20)
);

CREATE TABLE Building(
	BuildingId INT UNIQUE NOT NULL PRIMARY KEY,
	CityId INT,
	Floors INT,
    FOREIGN KEY(CityId) REFERENCES City(CityId)
);
ALTER TABLE Building
ADD BuildingName VARCHAR(100);

CREATE TABLE ElevatorModel(
	ElevatorModelId SERIAL NOT NULL PRIMARY KEY,
	ModelName VARCHAR(50),
	Speed INT,
	MaxWeight INT,
	PeopleLimit INT,
	ElevatorTypeId INT, 
	FOREIGN KEY(ElevatorTypeId) REFERENCES ElevatorType(ElevatorTypeId)
);

CREATE TABLE Elevator(
	ElevatorId SERIAL NOT NULL PRIMARY KEY,
	InstallationDate Date,
	BuildingId INT,
	FOREIGN KEY(BuildingId) REFERENCES Building(BuildingId),
	ElevatorModelId INT,
	FOREIGN KEY(ElevatorModelId) REFERENCES ElevatorModel(ElevatorModelId)
);

CREATE Table Technician(
	EmployeeId SERIAL NOT NULL PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	EmailAddress VARCHAR(50),
	AnnualSalary INT,
	SpecialSkill VARCHAR(100),
	EmployeeStatusId INT,
	FOREIGN KEY(EmployeeStatusId) REFERENCES EmployeeStatus(EmployeeStatusId)	
);

CREATE TABLE ServiceActivity(
	ServiceActivityId SERIAL NOT NULL PRIMARY KEY,
	EmployeeId INT,
	FOREIGN KEY(EmployeeId) REFERENCES Technician(EmployeeId),
	ElevatorId INT,
	FOREIGN KEY(ElevatorId) REFERENCES Elevator(ElevatorId),
	ServiceDateTime Date,
	ServiceDescription VARCHAR(500),
	ServiceStatusId INT,
	FOREIGN KEY(ServiceStatusId) REFERENCES ServiceStatus(ServiceStatusId)
);

-- Insert data
INSERT INTO CITY(CITYNAME) VALUES ('STOCKHOLM'), ('MALMÖ'), ('GÖTEBORG'), ('UMEÅ'), ('VÄSTERÅS'), ('SUNDSVALL'), ('GÄVLE'), ('VISBY') 

INSERT INTO ElevatorType(TypeName) VALUES ('Personhiss'), ('Varuhiss'), ('Plattformshiss'), ('Småvaruhiss'), ('Sänghiss'), ('Bilhiss'), ('Brandbekämpningshiss')

INSERT INTO EmployeeStatus(StatusDescription) VALUES ('active'), ('inactive')

INSERT INTO ServiceStatus(StatusDescription) VALUES ('completed'), ('not completed');

INSERT INTO ServiceStatus(StatusDescription) VALUES ('upcoming');

INSERT INTO Building VALUES (100, 1, 7), (101, 6, 2), (102, 5, 4);
INSERT INTO Building VALUES
(103, 2, 10),
(104, 3, 5),
(105, 4, 8),
(106, 5, 12),
(107, 6, 6),
(108, 1, 15),
(109, 2, 4),
(110, 3, 9),
(111, 4, 7),
(112, 5, 11),
(113, 6, 3),
(114, 1, 14);

INSERT INTO Elevator (InstallationDate, BuildingId, ElevatorModelId) VALUES
('2020-01-15', 100, 1),
('2021-03-22', 101, 2),
('2019-07-10', 102, 3),
('2022-05-05', 103, 4),
('2020-11-30', 104, 5),
('2021-08-18', 105, 6),
('2018-12-01', 106, 7),
('2023-02-14', 107, 1),
('2022-09-09', 108, 2),
('2020-06-25', 109, 3),
('2021-12-12', 110, 4),
('2019-04-04', 111, 5),
('2023-01-20', 112, 6),
('2022-03-17', 113, 7),
('2020-10-28', 114, 1),
('2021-05-19', 100, 2),
('2019-08-23', 101, 3),
('2022-07-07', 102, 4),
('2020-02-11', 103, 5),
('2021-09-15', 104, 6);


INSERT INTO ElevatorModel(ModelName, Speed, MaxWeight, PeopleLimit, ElevatorTypeId)
VALUES
('Kone SwiftLift 300', 90, 800, 10, 1),
('Otis Gen2 Comfort', 120, 1000, 13, 1),
('Schindler Cargo 5000', 30, 5000, 5, 2),
('Aritco HomeLift', 9, 400, 5, 3),
('Stannah MediLift', 60, 1600, 21, 4),
('Thyssenkrupp Evo 100', 100, 800, 10, 1),
('Cibes Cargo Heavy', 25, 2500, 3, 2);

INSERT INTO Technician (FirstName, LastName, EmailAddress, AnnualSalary, SpecialSkill, EmployeeStatusId) VALUES
('Anna', 'Svensson', 'anna.svensson@example.com', 42000, 'Hydraulics', 1),
('Björn', 'Karlsson', 'bjorn.karlsson@example.com', 39000, 'Control Systems', 1),
('Carina', 'Lindberg', 'carina.lindberg@example.com', 41000, 'Welding', 1),
('David', 'Eriksson', 'david.eriksson@example.com', 43000, 'Diagnostics', 2),
('Eva', 'Nilsson', 'eva.nilsson@example.com', 40000, 'Modernization', 1),
('Fredrik', 'Johansson', 'fredrik.johansson@example.com', 41500, 'Emergency Repairs', 2),
('Greta', 'Andersson', 'greta.andersson@example.com', 40500, 'Safety Inspections', 1),
('Henrik', 'Berg', 'henrik.berg@example.com', 39500, 'Software Updates', 1),
('Ingrid', 'Persson', 'ingrid.persson@example.com', 42000, 'Electrical Systems', 2),
('Jonas', 'Olofsson', 'jonas.olofsson@example.com', 40000, 'Preventive Maintenance', 1);

INSERT INTO ServiceActivity (EmployeeId, ElevatorId, ServiceDateTime, ServiceDescription, ServiceStatusId) VALUES
(1, 1, '2024-01-10', 'Routine maintenance and lubrication', 1),
(2, 2, '2024-01-15', 'Control system diagnostics', 1),
(3, 3, '2024-01-20', 'Welding repair on elevator shaft', 2),
(4, 4, '2024-02-05', 'Emergency stop button replacement', 1),
(5, 5, '2024-02-12', 'Modernization assessment', 3),
(6, 6, '2024-02-18', 'Emergency repair after power outage', 1),
(7, 7, '2024-03-01', 'Safety inspection and report', 1),
(8, 8, '2024-03-10', 'Software update to latest version', 1),
(9, 9, '2024-03-15', 'Electrical system check', 2),
(10, 10, '2024-03-20', 'Preventive maintenance', 3),
(1, 11, '2024-03-25', 'Cabin lighting replacement', 1),
(2, 12, '2024-04-01', 'Control panel cleaning', 1),
(3, 13, '2024-04-05', 'Welding minor cracks', 1),
(4, 14, '2024-04-10', 'Diagnostics for door malfunction', 2),
(5, 15, '2024-04-15', 'Modernization follow-up', 3),
(6, 1, '2024-04-20', 'Elevator pit cleaning', 1),
(7, 2, '2024-04-25', 'Inspection of safety brakes', 1),
(8, 3, '2024-05-01', 'Replacement of worn cables', 2),
(9, 4, '2024-05-05', 'Annual safety certification', 1),
(10, 5, '2024-05-10', 'Upgrade to energy-efficient lighting', 3),
(1, 6, '2024-05-15', 'Door sensor adjustment', 1),
(2, 7, '2024-05-20', 'Hydraulic fluid replacement', 1),
(3, 8, '2024-05-25', 'Inspection after reported noise', 2),
(4, 9, '2024-06-01', 'Control system firmware update', 1),
(5, 10, '2024-06-05', 'Final inspection after modernization', 1);

UPDATE Building SET BuildingName = 'Central Plaza' WHERE BuildingId = 100;
UPDATE Building SET BuildingName = 'Westside Towers' WHERE BuildingId = 101;
UPDATE Building SET BuildingName = 'Lakeside Apartments' WHERE BuildingId = 102;
UPDATE Building SET BuildingName = 'Skyline Heights' WHERE BuildingId = 103;
UPDATE Building SET BuildingName = 'Greenfield House' WHERE BuildingId = 104;
UPDATE Building SET BuildingName = 'Sunset Residences' WHERE BuildingId = 105;
UPDATE Building SET BuildingName = 'Riverside Complex' WHERE BuildingId = 106;
UPDATE Building SET BuildingName = 'City Center Offices' WHERE BuildingId = 107;
UPDATE Building SET BuildingName = 'Parkview Tower' WHERE BuildingId = 108;
UPDATE Building SET BuildingName = 'Harbor Point' WHERE BuildingId = 109;
UPDATE Building SET BuildingName = 'Mountain View' WHERE BuildingId = 110;
UPDATE Building SET BuildingName = 'Elm Street House' WHERE BuildingId = 111;
UPDATE Building SET BuildingName = 'Willow Court' WHERE BuildingId = 112;
UPDATE Building SET BuildingName = 'Birch Block' WHERE BuildingId = 113;
UPDATE Building SET BuildingName = 'Oak Residence' WHERE BuildingId = 114;

-- List all buildings with their city names
SELECT BuildingName, CityName
FROM Building b JOIN City c
ON b.cityId = c.cityId;

-- Show all elevators with their building name and ModelName
SELECT e.ElevatorId, b.BuildingName, m.ModelName
FROM Elevator e JOIN ElevatorModel m
ON e.ElevatorModelId = m.ElevatorModelId
JOIN Building b
ON e.buildingId = b.BuildingId;

-- List all service activities with technician name, elevatorid and service status
SELECT a.ElevatorId, CONCAT(t.FirstName, ' ', t.LastName),
s.StatusDescription, a.ServiceDescription
FROM ServiceActivity a JOIN Technician t
ON a.EmployeeId = t.EmployeeId
JOIN ServiceStatus s
ON a.ServiceStatusId = s.ServiceStatusId
ORDER BY a.ElevatorId;

-- Show all technicians with their employee status
SELECT t.EmployeeId, CONCAT(t.FirstName, ' ', t.LastName),
e.StatusDescription
FROM Technician t JOIN EmployeeStatus e
ON e.EmployeeStatusId = t.EmployeeStatusId
ORDER BY EmployeeId;

-- List all elevators, their building and the city they are in
SELECT e.ElevatorId, ModelName, e.BuildingId, b.BuildingName, c.CityName
FROM Elevator e 
JOIN Building b ON e.BuildingId = b.BuildingId
JOIN City c ON b.CityId = c.CityId
JOIN ElevatorModel m ON e.ElevatorModelId = m.ElevatorModelId




