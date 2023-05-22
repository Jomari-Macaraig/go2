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
### 1. Clone the project
```commandline
$ git clone <repo-url> go2
$ cd go2
```
### 2. Setting environment variable.
Please see env.template for environment variable to be setup for the project

### 3. Create virtual environment and install requirements.

### 4. Initialize database.
```commandline
$ make initialize_database
```
### 5. Run migration
```commandline
$ python manage.py migrate
```

### 6. Run development server
```commandline
python manage.py runserver
```

### Running standalone services
#### Postgres
```commandline
$ docker-compose -f compose/development.yml run -d --rm --name postgres --service-ports postgres
```