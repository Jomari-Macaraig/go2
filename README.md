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


## Setting up development
### 1. Cloning the project.
```commandline
$ git clone <repo-url> go2
$ cd go2
```

### 2. Initialize database and rabbitmq.
This will create user. Please omit this if done previously  
Please see env.template for environment variables to be configured for the project.  
Replace some environment variables for the meantime(we're using __0.0.0.0__ for local setup)
```commandline
$ export POSTGRES_HOST=0.0.0.0
$ export RABBITMQ_HOST=0.0.0.0
```
Run command
```commandline
$ make initialize_database
$ make initialize_rabbitmq
```

### 3. Spin up web, postgres and rabbitmq services.
```commandline
$ docker-compose -f compose/development.yml run --rm --name dev-go2-web --service-ports web /bin/bash
$ su go2
```

### 4. Set environment variables.
Please see env.template for environment variables to be configured for the project.  
Don't use the previous environment variables, replace it with
```commandline
$ export POSTGRES_HOST=postgres
$ export RABBITMQ_HOST=rabbitmq
```

### 5. Run migration.
```commandline
$ python manage.py migrate
```

### 6. Create tmux session
Create three tmux session for the ff
- development server
- celery worker
- dummy smtp  

Please check [this](https://tmuxcheatsheet.com/) cheat sheet to do that.

### 6. Run development server.
Attach to one tmux session to run the development server
```commandline
$ python manage.py runserver 0.0.0.0:8000
```

### 8. Run celery worker.
Attach to one tmux session to run celery worker
```commandline
$ celery -A config worker --loglevel=INFO
```

### 9. Run dummy smtp.
Attach to one tmux session to run aiosmtpd
```commandline
$ aiosmtpd -n -l ${EMAIL_HOST}:${EMAIL_PORT}
```

### 10. Create django admin superuser.
Detach to the tmux session and createsuper user.
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
Stop the container, increase the sleep count in the Makefile and rerun again.