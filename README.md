# recordingregx

## Getting started
### MacOS
```
python3 -m venv venv
```

```
source venv/bin/activate 
```

```
pip install -r requirements.txt 
```

```
cd recordingregx && python3 manage.py runserver
```

## HowTo  
- Missing Tables
- syncronize database and migrate again
```
python manage.py migrate --run-syncdb 

python manage.py migrate
```
- Create new app
```
python manage.py startapp appName
```