#!/bin/bash

psql postgresql://"$POSTGRES_SUPER_USER":"$POSTGRES_SUPER_USER_PASSWORD"@"$POSTGRES_HOST":"$POSTGRES_PORT" <<-EOSQL
    CREATE USER $POSTGRES_USER WITH PASSWORD '$POSTGRES_PASSWORD';
    CREATE DATABASE $POSTGRES_DB;
    GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $POSTGRES_USER;
    GRANT ALL ON SCHEMA public TO $POSTGRES_USER;
    GRANT ALL ON SCHEMA public TO public;
    ALTER DATABASE $POSTGRES_DB OWNER TO $POSTGRES_USER;
EOSQL