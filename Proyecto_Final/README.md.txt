Proyecto Final – Introducción a Ciencia de Datos 2026-I

Autor: Danilo Augusto Ardila Martínez

Descripción

Implementación de una base de datos relacional sobre la Copa del Mundo de Fútbol, a partir de archivos CSV. El modelo integra información de torneos, partidos, equipos, jugadores, goles, premios, estadios y entidades geográficas y deportivas.

Tecnologías
MySQL / MariaDB
XAMPP
phpMyAdmin
SQL
CSV
Git / GitHub
Ejecución de la base de datos
Iniciar MySQL/MariaDB desde XAMPP.
Abrir http://localhost/phpmyadmin.
Crear la base de datos:
CREATE DATABASE copaMundo
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
Ejecutar el script SQL del proyecto.
Carga de datos

Los datos se cargan desde archivos .csv mediante LOAD DATA INFILE, utilizando:

FIELDS TERMINATED BY ';'

Los archivos deben estar ubicados en la ruta definida en las instrucciones de carga.

Modelo relacional

El proyecto implementa claves primarias y foráneas, asegurando la integridad referencial entre las entidades del modelo.

Estructura
Proyecto final/
├── README.md
├── Diagrama_ER.png
├── conexionDB.py
├── datasets/
	├── awards.csv
	├── award_winners.csv
	├── city.csv
	├── confederations.csv
	├── country.csv
	├── federation.csv
	├── goals.csv
	├── matches.csv
	├── player_appearances.csv
	├── players.csv
	├── positions.csv
	├── regions.csv
	├── stadiums.csv
	├── teams.csv
	├── tournaments.csv
├── datasets/crudos/
	├── awards.csv
	├── award_winners.csv
	├── confederations.csv
	├── goals.csv
	├── matches.csv
	├── player_appearances.csv
	├── players.csv
	├── Query
	├── stadiums.csv
	├── teams.csv
	├── tournaments.csv