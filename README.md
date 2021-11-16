# Plant-Webapp
## Executive Summary
This web application was designed to act in conjunction with one of of my previously developed IoT apps as a form of central database, information terminal, and potentially eventually a control system.

## Installation
```bash
docker-build .
docker-compose run django bash
#python manage.py migrate
#python manage.py createsuperuser
```
Windows: navigate to directory in powershell
```
docker-build
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

* Implement user accounts or allowed IP address to limit who has access
* implement database backup, and Database update sanity checks
* require all admins login credentials to be non-standard usernames and passwords 

## Diagrams

**mockup**

![Front Page](https://github.com/abladow/Plant-Webapp/blob/master/planterfrontpage.png)
![Planter Page](https://github.com/abladow/Plant-Webapp/blob/master/planterpage.png)

**Architecture**

Context diagram
![Context](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
containers diagram
![Containers](https://github.com/abladow/Plant-Webapp/blob/master/images/containers.png)
components diagram
![components](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
