
# Web services and applications (WSAA) project 
Code for Web services and applications (WSAA) project with lecturer Andrew Beatty 
Semester 2, Higher Diploma in Science in Data Analytics at ATU, Galway, 2023/24. 
Author: Shane Keenan 


## About 
 

the database primary_schools was created in MySQL. It contains two tables university and school. 
university table is for the base version of the project (same as bookviewer).

  Flask server university_server.py along with the database access object UniversityDAO.py, queries the database, provides a RESTful API to interact with the university table in MySQL database
  and the client-side web interface, using AJAX calls, to perform these CRUD operations on the database  

a second web interface was developed - mo_scoil.html. this was to interact with the school table in the primary_school database. 
mo_scoil.html was my attempt at making the web interface pretty and improve the functionality but also provide a useful service. I haven't finished this off but it was starting to come together. 
I spent way too much time on making it look nice and function well and not enough time actually linking it to the database. So it doesn't have a RESTFUL API for it yet. 



## MySQL code 



CREATE DATABASE primary_schools;
USE primary_schools;


show tables; 
describe school;
describe university;
select * from school; 
select * from university; 

CREATE TABLE university (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    number_of_pupils INT NOT NULL
);



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


INSERT INTO university (name, address, number_of_pupils) VALUES 
('University College Dublin', 'Belfield, Dublin 4', 33000),
('Trinity College Dublin', 'College Green, Dublin 2', 18000),
('National University of Ireland, Galway', 'University Road, Galway', 18000),
('University College Cork', 'College Road, Cork', 22000);

-- in CMD 
-- "C:\Program Files\MySQL\MySQL Server 8.3\bin\mysql.exe" --local-infile=1 -u root -p root
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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random 
from PIL import Image
import os

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import random 
import os
from scipy.stats import norm





















# Topic02 Representing Data

Assignment
Using the URL below
https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m
Write a python program called currentweather.py that will print out the current temperature on the console (and only the temperature)
I have set the lat/long to my location, you may use that or a different location.
Last few marks:
Look at the documentation (below) and print out the current wind direction (10m) as well.
🌤️ Free Open-Source Weather API | Open-Meteo.com

Status: complete 
Date: 17/11/2023


# Topic03 Data Transfer

Assignment 
Quiz - HTTP and URLs 
status: complete - 100 % yeah !  
date: 23/02/2024


# Assignment 3 from Topic 04 Reading apis in the wild

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, and stores it into a file called "cso.json".
Upload this program to the same repository you used for the XML assignment
Save this assignment as "assignment03-cso.py"
This program should not be a long one
I don't need you to reformat or analyse the data in any way
It should be about 10ish lines long (I have not counted)
You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.



# Assignment 04 from Topic 05 Authentication

Write a program in python that will read a file from a repository, 
The program should then replace all the instances of the text "Andrew" with your name. 
The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
I do not need to see your keys (see lab2, to follow)
Handup: Push the program as assignment04-github.py to assignments repository.
Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.



