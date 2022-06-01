# Data Modeling with Postgres

## Project Description

The goal of this project to build a PostgreSQL database

## Database design

![alt text](https://github.com/tuan261220/Data-Modeling-with-Postgres-Udacity/blob/main/star_schema.png?raw=true)

- Fact table : songplays
- Dimension tables: songs, artist, users, time
## Project Repository files

The source code is available in three separate **Python** scripts. Below is a brief description of the main files:

1. `sql_queries.py` has all the queries needed to both create/drop tables for the database and the the query for insert new entry for other table
2. `create_tables.py` creates the database and creates/drops all the tables required using sql_queries module.
3. `etl.py` build the pipeline that exports the data from JSON files in DATA folder and transforms (exp : timestamp to date, week, hour, month,...) and insert all the data into the table


## Run step by Step:
- python create_tables.py
- python etl.py
