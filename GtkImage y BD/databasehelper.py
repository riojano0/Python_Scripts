#! /usr/bin/env python
# -*- coding: utf-8 -*-
from examples import starks
from sqlalchemy import Column, Integer, Binary, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker

engine = None
Base = declarative_base()


# The character table
class Character(Base):
	__tablename__ = "character"
	id_person = Column(Integer, primary_key=True)
	name = Column(String(20))
	picture = Column(Binary)

	def __repr__(self):
		return "<Stark Name:{}>".format(self.name)


class Database():
	def __init__(self):

		self.existsStark = False

		self.startDatabase()

		self.Session = sessionmaker(bind=self.engine)
		self.session = self.Session()

		if not self.existsStark:
			self.insertData()

	# Start the creation (or not) of the database
	def startDatabase(self):

		if not database_exists('sqlite:///ImageExample.db'):
			print 'Creating database'
			self.engine = create_engine('sqlite:///ImageExample.db')
			print 'Create Tables'
			Base.metadata.create_all(self.engine)
			print 'Insert examples'
		else:
			self.existsStark = True
			self.engine = create_engine('sqlite:///ImageExample.db')
			print 'Not Creating database'

	# Insert the examples in the table
	def insertData(self):

		for character in starks:
			person = Character(id_person=character[0], name=character[1], picture=character[2])
			self.session.add(person)

		self.session.commit()

	def getSession(self):
		return self.session

	def getQueryCharacter(self):
		return self.session.query(Character)

	def getCharacterImage(self, id):
		return self.getQueryCharacter().filter(Character.id_person == id).all()[0]


if __name__ == "__main__":
	Database()
	print "Database activities"
