SHELL := /bin/bash

.PHONY:
	clean
	initialize_database

help:
	@echo "clean - remove all artifacts"

clean:
	find . -iname "*.pyo" | xargs rm -Rf
	find . -iname "*.pyd" | xargs rm -Rf
	find . -iname "__pycache__" | xargs rm -Rf
	find . -iname "*.pyc" | xargs rm -Rf


initialize_database:
	make clean
	docker-compose -f compose/development.yml run -d --rm --name postgres --service-ports postgres
	sleep 1
	. scripts/build/database/create_user_and_db.sh
	docker stop postgres
