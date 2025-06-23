CREATE TABLE Regions (
    region_id INT PRIMARY KEY, 
    region_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE Countries (
    country_id INT PRIMARY KEY,
    country_name VARCHAR(50) UNIQUE NOT NULL,
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES Regions(region_id)
);

INSERT INTO Regions VALUES 
    (1, 'Europe'),
(2, 'Africa'), (3, 'Asia'), (4, 'Australia'), (5, 'Antarctica'), (6, 'South America'), (7, 'North America');

INSERT INTO Countries VALUES
(1, 'Australia', 4),
(2, 'Bangladesh', 3),
(3, 'Canada', 7),
(4, 'Djibouti', 2),
(5, 'Equador', 6),
(6, 'France', 1),

