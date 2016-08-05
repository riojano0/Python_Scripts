#! /usr/bin/env python
# -*- coding: utf-8 -*-
from databasehelper import Database
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class MainWindow(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="ImageRefresh from database")
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_border_width(0)
		self.set_default_size(700, 600)
		self.set_resizable(False)

		self.database = Database()
		self.session = self.database.getSession()
		self.characters = self.database.getQueryCharacter()
		self.person_store = Gtk.ListStore(int, str)
		self.imgPerson = Gtk.Image()

		GridMain = Gtk.Grid()
		GridMain.set_column_homogeneous = False

		GridMain.attach(self.personviews(), 0, 0, 1, 1)
		GridMain.attach(self.showimage(), 1, 0, 2, 1)

		self.add(GridMain)

	def personviews(self):
		try:
			rows = self.characters.all()
			for row in rows:
				self.person_store.append([row.id_person, row.name])

			person_treeview = Gtk.TreeView(self.person_store)
			person_treeview.set_hexpand(True)
			person_treeview.set_vexpand(True)

			for i, col_title in enumerate(["ID", "Name"]):
				# Render means how to draw the data
				renderer = Gtk.CellRendererText()
				# create columns
				column = Gtk.TreeViewColumn(col_title, renderer, text=i)
				# Order By
				column.set_sort_column_id(i)
				# add column to treeview
				person_treeview.append_column(column)

			selected_row = person_treeview.get_selection()
			selected_row.connect("changed", self.item_selected_person)

			frame = Gtk.Frame()
			frame.add(person_treeview)
			return frame

		except:
			self.session.close()

	def showimage(self):
		frame = Gtk.Frame()
		# Load default image
		imagenPixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale('img/default.jpg', 150, 150, False)
		self.imgPerson.set_from_pixbuf(imagenPixbuf)
		label = Gtk.Label("Person Selected")
		box = Gtk.VBox()
		box.add(label)
		box.add(self.imgPerson)

		frame.add(box)

		return frame

	def item_selected_person(self, selection):
		model, row = selection.get_selected()
		id = str(model[row][0])

		try:
			pictureCath = self.database.getCharacterImage(id)
			image = pictureCath.picture

			loader = GdkPixbuf.PixbufLoader()
			loader.set_size(200, 150)
			loader.write(image)
			loader.close()
			pixbuf = loader.get_pixbuf()

			# Load image from database
			self.imgPerson.set_from_pixbuf(pixbuf)

		except:
			self.session.close()

		finally:
			self.session.close()


if __name__ == "__main__":
	window = MainWindow()
	window.show_all()
	window.connect("delete-event", Gtk.main_quit)
	Gtk.main()
