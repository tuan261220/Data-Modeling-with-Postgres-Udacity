# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                            songplay_id integer CONSTRAINT songplay_id_pk PRIMARY KEY,
                            start_time timestamp NOT NULL,
                            user_id integer NOT NULL,
                            level varchar(100), 
                            song_id varchar(100),
                            artist_id varchar(100),
                            session_id integer,
                            location varchar(100),
                            user_agent varchar(4000))
                        """)

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (
                          user_id integer CONSTRAINT user_id_pk PRIMARY KEY,
                          first_name varchar(100),
                          last_name varchar(100),
                          gender varchar(1),
                          level varchar(100))
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (
                           song_id varchar(100) CONSTRAINT song_id_pk PRIMARY KEY,
                           title varchar(100) NOT NULL,
                           artist_id varchar(100),
                           year integer NOT NULL,
                           duration double precision NOT NULL)
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
                            artist_id varchar(100) CONSTRAINT artist_id_pk PRIMARY KEY,
                            name varchar(100) NOT NULL,
                            location varchar(100),
                            latitude double precision,
                            longitude double precision )
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
                            start_time timestamp,
                            hour integer,
                            day integer,
                            week integer,
                            month integer,
                            year integer,
                            weekday integer)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                             ON CONFLICT (songplay_id) DO NOTHING;
                        """)

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)
                         VALUES (%s, %s, %s, %s, %s)
                         ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
                    """)

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration)
                         VALUES (%s, %s, %s, %s, %s)
                         ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, name, location, latitude, longitude)
                           VALUES (%s, %s, %s, %s, %s)
                           ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                         VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""  SELECT s.song_id, a.artist_id 
                FROM songs s 
                JOIN artists a 
                ON s.artist_id = a.artist_id 
                WHERE s.title = %s and a.name = %s and s.duration = %s; 
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]