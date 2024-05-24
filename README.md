
# Web services and applications (WSAA) project 
Code for Web services and applications (WSAA) project with lecturer Andrew Beatty 
Semester 2, Higher Diploma in Science in Data Analytics at ATU, Galway, 2023/24. 
Author: Shane Keenan 


## About 
 
the database ``primary_schools`` was created in MySQL. It contains two tables ``university`` and ``school``. 
university table is for the base version of the project (same as bookviewer).

  Flask server ``university_server.py`` along with the database access object ``UniversityDAO.py``, queries the database, provides a RESTful API to interact with the university table in MySQL database
  and the client-side web interface, using AJAX calls, to perform these CRUD operations on the database  

a second web interface was developed - ``mo_scoil.html``. this was to interact with the ``school`` table in the ``primary_school`` database. 

mo_scoil.html was my attempt at making the web interface pretty and improve the functionality but also provide a useful service. 
mo_scoil uses - ``school_server.py`` and ``SchoolDAO.py`` 

mo_scoil sources data from the Gov.ie website. The data itself was only avaialable as .csv files so I have imported this data from ``schools.csv`` into the MySQL database and setup the table using the commands shown below. 

standard CRUD functions are available for this database. But also search functions to allow the user to find a school they are interested in. 



## MySQL code 

CREATE DATABASE primary_schools;
USE primary_schools;


show tables; 
describe school;
describe university;
describe book;
select * from school; 
select * from university; 
select * from book; 

CREATE TABLE university (
    ID INT PRIMARY KEY,
    name VARCHAR(255) ,
    address VARCHAR(255),
    number_of_pupils INT
);

CREATE TABLE book (
    ID INT PRIMARY KEY,
    title VARCHAR(255) ,
    author VARCHAR(255),
    price INT 
);


SELECT id FROM school ORDER BY id ASC LIMIT 1;

SELECT COUNT(*) FROM school;

CREATE TABLE school (
    academic_year_enrolment INT,  
    roll_number INT PRIMARY KEY,  -- Roll number is the unique identifier for each school - primary key
    official_name VARCHAR(255) NOT NULL,
    address_line1 VARCHAR(255),
    address_line2 VARCHAR(255),
    address_line3 VARCHAR(255),
    address_line4 VARCHAR(255),
    county_description VARCHAR(100),
    eircode VARCHAR(10),
    school_latitude INT,  
    school_longitude INT,  
    email VARCHAR(100),
    phone_no VARCHAR(20),
    principal_name VARCHAR(255),
    local_authority_description VARCHAR(100),
    deis ENUM('Y', 'N'),  
    irish_classification_description VARCHAR(100),
    gaeltacht_indicator ENUM('Y', 'N'),  
    island ENUM('Y', 'N'),  
    ethos_description VARCHAR(100),
    female INT,  
    male INT,  
    total INT  
);


INSERT INTO university (ID, name, address, number_of_pupils) VALUES 
('1','University College Dublin', 'Belfield, Dublin 4', 33000),
('2','Trinity College Dublin', 'College Green, Dublin 2', 18000),
('3','National University of Ireland, Galway', 'University Road, Galway', 18000),
('4','University College Cork', 'College Road, Cork', 22000);

INSERT INTO book (ID, title, author, price) VALUES 
('1', 'Lord of the Rings', 'J.R.R. Tolkien', 33000);

-- in CMD 
-- "C:\Program Files\MySQL\MySQL Server 8.3\bin\mysql.exe" --local-infile=1 -u root -p ashtrA123xyz!
set global local_infile = 1;
show variables like "%infile%";



show variables like "%secure_file_priv%";

LOAD DATA LOCAL INFILE "C:/Users/shane/Desktop/HDip in Data Analytics/Sesmester 3/Applied Databases/scripts/schools.csv"
INTO TABLE school
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;




## Running the code 

steps to create:  

1. Install Anaconda 
2. Install visual studio code 
3. create a github account 
4. create public repository "WSAA-coursework" with README.md and .gitignore file
5. Sign into github using VScode 
6. Clone repository to PC 
7. Create necesary folders and files
8. Commit all and push to repo 

## Required python packages







