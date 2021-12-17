# Plant-Webapp
## Executive Summary
This web application was designed to act in conjunction with one of of my previously developed IoT apps as a form of central database, information terminal, and potentially eventually a control system. The previous app allowed for realtime monitoring and control of a Aeroponic plant box for urban agriculture, and comes with a built in web interfaces but it is unable to store or display the information from multiple control devices. This Web app attempts to fix this by acting as a central database and access point.

## Installation
```bash
docker-build .
docker-compose run django bash
#python manage.py migrate
#python manage.py createsuperuser
```
Windows: navigate to directory in powershell
```bash
docker-build .
docker-compose run django bash
#python manage.py migrate
#python manage.py createsuperuser
```

## Getting Started
To run my plant app,
```bash
docker-compose up
```
Windows: navigate to directory in powershell
```
docker-compose up
```
Current prototype version has admin pages, and pages asociated with the databases

Key webaddresses
./api/plant/
./api/plant/<plant#>/
./api/species/
./api/species/<species#>/
./admin

### Current server address
http://35.224.151.11/

testing login: admin for both

## User Stories

-As an Administrator I want to be edit plant database so I can add or remove individual plants.

-As an Administrator I want to be edit Species database so I can add or remove types of plants that my system needs to track.

-As a User I want to be able to view the current state of a given plant or tray so I can be able to monitor any given plant in real time

## Acceptance criteria

* Must allow Admins to edit the current database of plants
* Must allow Admins to edit the current list of recorded Species
* Must allow a User to access the plant or tray's data for any given plant in real time
## Misuser Stories

-As a competiter, I want to be able to view the information for each plant so I can take their competitive advantage

-As a hacker, I want to send false HTTP packets into the database so I can poison the whole database

-As a rural agriculture lobbyist, I want gain access to admin logins so I can destroy all the collected plant data
 
## Mitigation criteria

* Implement user accounts or allowed IP address to limit who has access - possible through google cloud firewall rules
* implement database backup, and Database update sanity checks - multiple validators and restrictions on databse and input
* require all admins login credentials to be non-standard usernames and passwords - current version has a strong password, additioanl policies possible 

## HTTP packet forming

{
    "id": [pk],
    "name": [[a-zA-Z0-9] for 1 to 500 chars],
    "age": [INT 1-52],
    "water": [INT 1-1000],
    "Humidity": [INT 0-100],
    "Light":[INT 1-10],
    "nutrient_amount": [INT 1-10],
    "tempurature": [INT 33-100],
    "species": [Specied FK]
}

## Diagrams

**mockup**

![Front Page](https://github.com/abladow/Plant-Webapp/blob/master/planterfrontpage.png)
![Planter Page](https://github.com/abladow/Plant-Webapp/blob/master/planterpage.png)

**Actual pages**
![Front Page](https://github.com/abladow/Plant-Webapp/blob/master/images/finalfront.PNG)
![Planter Pag](https://github.com/abladow/Plant-Webapp/blob/master/images/finalmain.PNG)

**Architecture**

Context diagram
![Context](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
containers diagram
![Containers](https://github.com/abladow/Plant-Webapp/blob/master/images/containers.png)
components diagram
![components](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
