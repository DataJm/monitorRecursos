from sqlalchemy import create_engine
engine = create_engine("sqlite:///logs.db")
# engine.execute('''
#     create table logs (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         date VARCHAR(50),
#         cpu FLOAT
#     )
# ''')

resultados = engine.execute("select * from logs")

for x in resultados:
    print(x)