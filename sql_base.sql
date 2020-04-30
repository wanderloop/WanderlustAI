#CREATE DATABASE GeneralUser;
#ID,IDNumber,long,lat,time,date
/*
CREATE TABLE PersonsData (
    ID int,
    IDNumber varchar(255),
    longitude float(20),
    latitude float(20),
    timeData varchar(255),
    dateData varchar(255),
    PRIMARY KEY(ID));
    
*/
/*
USE GeneralUser;
SHOW TABLES; show tables
SHOW FULL TABLES; show tables along with format
SHOW COLUMNS FROM PersonsData; show just collum fro the table
SELECT * FROM PersonsData; show the data that is the table
SET SQL_SAFE_UPDATES = 0; set to allow delete
DELETE FROM PersonsData;  delete all data in table
ALTER TABLE PersonsData ADD COLUMN date2 VARCHAR(255) AFTER date1; alter table add a collumn
SELECT * FROM PersonsData WHERE date1=1 and ID =2; to search for an object with row specified
SELECT ID FROM PersonsData WHERE IDNumber='+923462333830';
SELECT COUNT(*) used to count rows
*/
#DELETE FROM PersonsData;
#SELECT * FROM PersonsData;
#ALTER TABLE PersonsData ADD COLUMN date2 VARCHAR(255) IF NOT EXISTS date2;

#SELECT * FROM PersonsData ORDER BY IDNumber;
#SELECT distinct IDNumber from PersonsData;
#SELECT * FROM PersonsData ORDER BY longitude,latitude;
#SELECT COUNT(*) FROM PersonsData
#ALTER TABLE PersonsData ADD COLUMN localID VARCHAR(255) AFTER ID;
#INSERT INTO PersonsData (localID) Values (1)
#SELECT * FROM PersonsData ORDER BY longitude DESC, latitude DESC


SELECT * FROM PersonsData;
