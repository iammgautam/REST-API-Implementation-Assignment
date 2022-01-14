# Backend Assignment

The REST API Implementation is done using Django Rest Framework.


## Deployment

To deploy the project:

1. Setup the File System

```bash
  mkdir project
  cd project
  git clone https://github.com/zengboi/REST-API-Implementation-Assignment.git
  cd REST-API-Implementation
```

2. Create a virtual environment.

```bash
python -m pip install virtualenv
virtualenv .env
source .env/bin/activate
```

3. Install all the package dependency

```bash
pip install -r requirements.txt
```

4. Setup Django Database & Admin Dependencies 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
5. Run the Server
```bash
python manage.py runserver
```

# Note:
1. API Endpoint Testing has been done using Postman.
