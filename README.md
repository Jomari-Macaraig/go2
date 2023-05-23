# Simple Ecommerce

## Requirements
Latest Docker Desktop
- [docker-desktop](https://docs.docker.com/desktop/)

or

Latest Docker and Docker Compose for your OS
- [docker-machine](https://docs.docker.com/engine/installation/)
- [docker-compose](https://docs.docker.com/compose/install/)

Postgresql for psql command
- [postgresql](https://www.postgresql.org/download/)

Python
- Python3.9

## Setting up development
### 1. Cloning the project.
```commandline
$ git clone <repo-url> go2
$ cd go2
```
### 2. Set environment variables.
Please see env.template for environment variables to be configured for the project

### 3. Create virtual environment and install requirements.
```commandline
$ virtualenv /venv/<name>
$ source /venv/<name>
$ pip install -r requirements/development.txt
```

### 4. Initialize database and rabbitmq.
This will create user. Please omit this if done previously
```commandline
$ make initialize_database
$ make initialize_rabbitmq
```

### 7. Start postgres and rabbitmq.
```commandline
$ make start_dev
```

### 6. Run migration.
```commandline
$ python manage.py migrate
```

### 7. Run development server.
```commandline
$ python manage.py runserver
```

### 8. Run celery worker.
Create another window. Set environment variable before executing command
```commandline
$ celery -A config worker --loglevel=INFO
```

### 9. Run dummy smtp.
Create another window. Set environment variable before executing command
```commandline
$ aiosmtpd -n -l ${EMAIL_HOST}:${EMAIL_PORT}
```

### 10. Create django admin superuser.
```commandline
$ python manage.py createsuperuser
```

### Running standalone services

#### Postgres
```commandline
$ docker-compose -f compose/development.yml run -d --rm --name postgres --service-ports postgres
```

#### Rabbitmq
```commandline
$ docker-compose -f compose/development.yml run -d --rm --name rabbitmq --service-ports rabbitmq 
```

### Troubleshooting
1. If you run an issue with running with
```commandline
$ make initialize_database
$ make initialize_rabbitmq
```
Try to update the sleep count in the Makefile.