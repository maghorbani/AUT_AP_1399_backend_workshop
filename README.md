## django example

#### prerequisites
* a proper version of python3
* the pip package manager
* [Optional] a python virtial environment tool *I'm using the python -m venv*

#### setting up the project
1. creating and activating the virtual environment (it can change based on the venv tool you use)
```
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
```
or in windows the 3rd line would be sth like: `./env/scripts/activate`
2. installing python packages listed in req.txt
```
pip install -r req.txt
```
3. migrating the database and creating the superuser
```
cd mysite&&python manage.py migrate
python manage.py createsuperuser
```

#### developement test and tools
1. to run webserver:
```
python manage.py runserver
```

2. to use the interactive django shell
```
python manage.py shell
```

3. to start a new app
```
python manage.py startapp [appname]
```