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

##  Stories

## Misuser Stories

## Acceptance criteria

## Mitigation criteria

## Diagrams

**mockup**

![Front Page](https://github.com/abladow/Plant-Webapp/blob/master/planterfrontpage.png)
![Planter Page](https://github.com/abladow/Plant-Webapp/blob/master/planterpage.png)

**architecure**
Context diagram
![Context](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
containers diagram
![Containers](https://github.com/abladow/Plant-Webapp/blob/master/images/containers.png)
components diagram
![components](https://github.com/abladow/Plant-Webapp/blob/master/images/context.png)
