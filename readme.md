# Sorting App
This App sorts an array of integers. You can choose one of sorting type and check out time of this sorting.
## Installation Guide
Clone this project to  your local machine with installed Docker.
</br> Execute next commands to create and run Docker containers:
* docker-compose up --build

Execute next commands to create superuser:
* docker exec -it sorting_app_web bash
* python manage.py createsuperuser