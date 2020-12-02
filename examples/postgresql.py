#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Solución para el Ejercicio 2 "SQLAlchemy" del Módulo 10

import sqlalchemy

# engine = sqlalchemy.create_engine('postgresql://usuariodb:abc@192.168.56.2:5432/municipios')
engine = sqlalchemy.create_engine('postgresql://postgres:abc@localhost:5432/municipios')
connection = engine.connect()


# Metadatos (info) de tablas
metadata = sqlalchemy.MetaData()
t = sqlalchemy.Table('municipio', metadata, autoload=True, autoload_with=engine)
# Nombres de columnas
print(t.columns.keys())
print()
# str(), o sea convertir a string (sin poner nada, print() ya lo usa) en este caso está
# pensado para solo escribir el nombre de la tabla; repr(), que es una alternativa a
# str() (...), en este caso lo han preparado para que dé la información completa 
print(repr(metadata.tables['municipio']))
print()


# Equivalenta a 'SELECT * FROM table_name'
# NOTA: pueden hacerse variaciones, como añadir cláusulas WHERE, etc. (...)
query = sqlalchemy.select([t])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)
