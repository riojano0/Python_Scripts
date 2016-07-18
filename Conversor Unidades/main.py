try:
	#Python 2
	from Tkinter import Tk, OptionMenu, Frame,Button, Label, LabelFrame, StringVar, Entry, E, END, W
except:
	#Python 3
	from tkinter import Tk, OptionMenu, Frame,Button, Label, LabelFrame, StringVar, Entry, E, END, W
from converclasses.c_long import *
from converclasses.c_almac import *
from PIL import Image, ImageTk
from resources.login import intro
import resources.resourceString as R

class Main():

	def __init__(self, master):

		#La intro se puede apagar al final, cumple solo una funcion vistosa

		#Iniciacion propia de la ventan y sus configuraciones
		self.master=master
		self.master.wm_title(R.AppTitle)
		self.widht=(self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
		self.height=(self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 2
		self.master.geometry("+{0:.0f}+{1:.0f}".format(self.widht, self.height))
		self.master.deiconify()
		self.master.resizable(False,False)
		self.icon=(R.IconPath)
		self.master.iconbitmap(self.icon)
		self.master.configure(background=R.Bgcolor)

		#Definicion de variables variables que estaran en uso.
		self.btnFlecha=Image.open(R.BtnFlechaImgPath)
		self.btnFlechaimg=ImageTk.PhotoImage(self.btnFlecha)
		self.selectMed = StringVar(self.master)
		self.selectMed.set(R.SelectMed)

		#Las variables que usaran para saber que hacer o que reemplazar
		self.fromLabel = StringVar()
		self.fromLabel.set(R.Select)
		self.toLabel=StringVar()
		self.toLabel.set(R.Select)

		#Los valores de las entradas
		self.fromNumber=StringVar()
		self.toNumber=StringVar()

		#La creacion de las partes del programita.
		self.menuChoices()
		self.convertChoice()
		self.convertButton()

	def menuChoices(self):

		#Menu de seleccion principal sobre los tipos que conversion que hara el programa
		self.MenuChoices = OptionMenu(self.master, self.selectMed, R.LongMain,R.AlmacMain, command=self.choice)
		self.MenuChoices.configure(bg="white",fg="black",activebackground="#eceefb",highlightbackground=R.Bgcolor,
									indicatoron=0,image=self.btnFlechaimg,compound='right')
		self.MenuChoices.grid(row=0,column=0)

	def convertChoice(self):

		#Las partes que integran el primer submenu llamado "DE", labelFrame,menu, entrada.
		self.labelFrameFrom=LabelFrame(self.master,text="De",background=R.Bgcolor)
		self.labelFrameFrom.grid(row=1,column=0,padx=5,pady=3)

		self.menuFrom=OptionMenu(self.labelFrameFrom,self.fromLabel,"",)
		self.menuFrom.configure(bg=R.White,fg=R.Black,activebackground=R.hoverBtnColor,highlightbackground=R.Bgcolor,
								indicatoron=0,image=self.btnFlechaimg, compound='right')
		self.menuFrom.grid(row=0,column=0,padx=3,pady=2,sticky=E)

		self.entryFrom=Entry(self.labelFrameFrom,justify='center',textvariable=self.fromNumber)
		self.entryFrom.grid(row=2,column=0,padx=5,pady=5)

		#Las partes que integran el segundo submenu llamado "Hasta", labelFrame, menu, entrada.

		self.labelFrameTo=LabelFrame(self.master,text="Hacia",background=R.Bgcolor)
		self.labelFrameTo.grid(row=1,column=1,padx=5,pady=3)

		self.menuTo=OptionMenu(self.labelFrameTo,self.toLabel,"",)
		self.menuTo.configure(bg=R.White,fg=R.Black, activebackground=R.hoverBtnColor,highlightbackground=R.Bgcolor,
					indicatoron=0,image=self.btnFlechaimg, compound='right')
		self.menuTo.grid(row=0,column=0, padx=3, pady=2, sticky=E)

		self.entryTo=Entry(self.labelFrameTo,justify='center',textvariable=self.toNumber,state="readonly")
		self.entryTo.configure(bg="red", readonlybackground=R.Bgcolor)
		self.entryTo.grid(row=2,column=0,padx=3,pady=5)

	def convertButton(self):
		#El boton Convertir que activa las funcionalidades de los campos
		self.butonimgpath = Image.open(R.BtnConvertirImgPath)
		self.butonTkImage = ImageTk.PhotoImage(self.butonimgpath)
		self.button = Button(self.master,text='Convertir',command=self.choiceFromTo)
		self.button.configure(image=self.butonTkImage, bd=False, highlightthickness=0, activebackground="black")
		self.button.grid(row=3,column=1,sticky=E)

	def choice(self, choices):
		#Al tocar el boton [<- Selecione] se cambia la opcion de medida y se genera opciones acorde
		# error.set("")
		#Opciones acorde en el caso de elegir "Longitudes"
		if choices==R.LongMain:
				self.fromLabel.set(R.LongStart)
				self.toLabel.set(R.LongStart)
				self.clean()
				# medidas= ("kms", "milla","metro","legua","yarda","pie")
				for m in R.LongList:
						self.menuFrom['menu'].add_command(label=m,command=lambda v=self.fromLabel,l=m:v.set(l))
				for m in R.LongList:
						self.menuTo['menu'].add_command(label=m,command=lambda v=self.toLabel,l=m:v.set(l))

		#Genera las opciones si se elige "Almacenamientos"
		elif choices==R.AlmacMain:
				self.fromLabel.set(R.AlmacStart)
				self.toLabel.set(R.AlmacStart)
				self.clean()
				# medidas= ("Gbs", "Mbs","Kbs","bytes")
				for m in R.AlmacList:
						self.menuFrom['menu'].add_command(label=m,command=lambda v=self.fromLabel,l=m:v.set(l))
				for m in R.AlmacList:
						self.menuTo['menu'].add_command(label=m,command=lambda v=self.toLabel,l=m:v.set(l))

	def choiceFromTo(self):
		
		try:
			#Se toma los valores de las seleciones [DE] y [HACIA], ademas de la entrada numerica
			# self.fromChoice=self.fromNumber.get()
			self.fromChoice=self.fromLabel.get()
			self.toChoice=self.toLabel.get()
			self.fromN=self.entryFrom.get()

			#A partir de un if se consulta
			#el objeto a crear que poseen los comportamientos de convertirse a 
			#otra medida

			#Si la medida esta en el campo de las longitudes
			if self.toChoice in R.LongList:
				convLong = Distancia(float(self.fromN))
				dicChoices = {0: convLong.km_a_(self.toChoice),
				 					1: convLong.milla_a_(self.toChoice),
			 	 					2: convLong.metro_a_(self.toChoice),
		 	 	 					3: convLong.legua_a_(self.toChoice),
	 	 	 	 					4: convLong.yarda_a_(self.toChoice),
 	 	 	 	 					5: convLong.pie_a_(self.toChoice)}

				self.toNumber.set(dicChoices.get(R.LongList.index(self.fromChoice)))

			#Si la medida esta en el campo de las medidas de almacenamiento
			elif self.toChoice in R.AlmacList:
				conAlmc = Almacenamiento(float(self.fromN))
				dicChoices = {0: conAlmc.gb_a_(self.toChoice),
								1: conAlmc.mb_a_(self.toChoice),
								2: conAlmc.kbs_a_(self.toChoice),
								3: conAlmc.bytes_a_(self.toChoice)}
				
				self.toNumber.set(dicChoices.get(R.AlmacList.index(self.fromChoice)))

		except:
			self.toNumber.set('{}'.format("Numero no valido"))


	def clean(self):
		self.menuTo['menu'].delete(0,END)
		self.menuFrom['menu'].delete(0,END)

if __name__ == "__main__":
	#La linea 'intro()' puede ser tranquilamente comentado, es algo vistoso que me hizo un amigo.
	intro()
	#Inicia el conversor
	root = Tk()
	main=Main(root)
	root.mainloop()
