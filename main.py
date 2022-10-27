# TODO: vamos a automatizar generar métricas de uso de CPU. 
# Vamos a guardar estas métricas para un análizis y monitoreo posterior. 
# Vamos a mandar eso a una base de datos. (sqlite)

# Importing the library
import psutil
from datetime import datetime
from sqlalchemy import create_engine

now       = datetime.now()
cpu_usage = psutil.cpu_percent(1)

engine = create_engine("sqlite:///logs.db")

print(f"{now} | {cpu_usage}")

query = f"insert into logs (date, cpu) values ('{now}', {cpu_usage})"

engine.execute(query)
