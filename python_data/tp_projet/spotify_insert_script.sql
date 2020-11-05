DROP TABLE Public."spotify";


CREATE TABLE Public."spotify" (
acousticness varchar(50), 
artists varchar(100),
danceability varchar(50),
duration_ms varchar(50),
energy varchar(50),
explicit varchar(50),
id varchar(80),
instrumentalness varchar(50),
key varchar(50),
liveness varchar(50),
loudness varchar(50),
mode varchar(50),
name varchar(200),
popularity varchar(50),
release_date varchar(50),
speechiness varchar(50),
tempo varchar(50),
valence varchar(50),
year varchar(50)
);

COPY Public."spotify" FROM '/home/victor/Documents/python_m2/python_data/tp_projet/data/data_spotify.csv' DELIMITER ',' CSV;

SELECT * FROM Public."spotify";

COPY Public."spotify" TO '/home/victor/Documents/python_m2/python_data/tp_projet/data/sportify_psql.csv' DELIMITER ',' CSV HEADER;