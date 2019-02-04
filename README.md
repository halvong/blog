Django2, Apress PDF
2/3, Sun
pg 39

#superuser
hal:hal

http://localhost:8000/admin

#steps
1. python manage.py migrate
2. python manage.py runserver
3. python manage.py startapp blogi
4. docker-compose exec web python manage.py makemigrations blogi 
5. docker-compose exec web python manage.py sqlmigrate blogi 0001
6. docker-compose exec web python manage.py migrate
7. docker-compose exec web python manage.py createsuperuser 
7. docker-compose exec web python manage.py shell 

