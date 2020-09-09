# kanban_backend
Install the requirements: 
```bash
pip install -r requirements.txt
```
Create Database and various credentials information(username,password) to work with Postgresql DB. Make those changes in settings.py
## Migrate the database:
```bash
python manage.py migrate
```
## For admin purpose Create Super User: 
```bash
python manage.py createsuperuser
```
For a new user, go to the admin panel and create user after login.
