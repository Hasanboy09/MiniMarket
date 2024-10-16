mig:
	./manage.py makemigrations
	./manage.py migrate

user:
	./manage.py createsuperuser

app:
	./manage.py startapp apps