import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

#Configuraciòn de la base de datos (XAAMP)
USER = "root"
PASSWORD = ""
HOST = "localhost"
PORT = "3306"
DATABASE = "copaMundo"

connection_string = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
try:
    engine = create_engine(connection_string)
    with engine.connect() as connection:
        pass # La conexión se ha establecido correctamente

except SQLAlchemyError as e:
    print (f"Error al conectar a la base de datos: {e}")
    print("Por favor validar que XAAMP esté encendido y el puerto sea correcto")
    exit (1)

csv_files = {
    'award_winners' : '../datasets/award_winners.csv',
    'awards' : '../datasets/awards.csv',
    'confederations' : '../datasets/confederations.csv',
    'goals' : '../datasets/goals.csv',
    'matches' : '../datasets/matches.csv',
    'player_appearances' : '../datasets/player_appearances.csv',
    'players' : '../datasets/players.csv',
    'stadiums' : '../datasets/stadiums.csv',
    'teams' : '../datasets/teams.csv',
    'tournaments' : '../datasets/tournaments.csv'
}

print("Iniciando el proceso de migración a MYSQL...")

for table_name, file_path in csv_files.items():
    if os.path.exists(file_path):
        print(f"Procesando archivo {file_path}")

        #Lectura del dataset (extracción)
        df = pd.read_csv(file_path, sep=";")

        # cargar datos en MUSQL
        try:
            df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
            print(f"Tabla {table_name} fue creada e importada con éxito")
        except Exception as e:
            print(f"Error al importar la tabla {table_name}")
    else:
        print(f'Archivo {file_path} no encontrado. Por favor verifica la ruta del archivo')

print("/ntodos los datos han sido migrados a XAAMP correctamente/n")