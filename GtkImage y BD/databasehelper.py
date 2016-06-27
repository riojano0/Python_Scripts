#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sqlite3
import io
from PIL import Image

# Query para generar la tabla
PersonTable = ("CREATE TABLE person (id_person INTEGER PRIMARY KEY NOT NULL, Name TEXT, picture BLOB)")

# Imagenes para el ejemplo, es necesario hacer esta conversion para que luego permita guardarlo como BLOB
path = ["img/john.jpg", "img/sansa.jpg", "img/brandon.jpg"]
imgs = []
for p in path:
	i = Image.open(p)
	stream = io.BytesIO()
	i.save(stream, format="JPEG")
	imgs.append(stream.getvalue())

# Lista de Ejemplo
People = [(1, "John", imgs[0]), (2, "Sansa", imgs[1]), (3, "Brandon", imgs[2])]


# Funcion usada para conectarse con la base de datos del otro lado
def connection():
	conn = sqlite3.connect("ImageExample.db")
	db = conn.cursor()
	return db

def start():
	conn = sqlite3.connect("ImageExample.db")
	db = conn.cursor()

	if os.path.isfile("ImageExample.db"):
		# This lines is only for reload the tables and examples
		#Estas lineas resetean los ejemplos/tablas

		print ("The Database Create, drop tables and reload examples")
		db.execute("DROP TABLE IF EXISTS person")
		db.execute(PersonTable)

		for person in People:
			db.execute("INSERT INTO person VALUES(?,?,?)", (person[0], person[1], sqlite3.Binary(person[2])))
			conn.commit()

		conn.close()

if __name__ == "__main__":
	start()

