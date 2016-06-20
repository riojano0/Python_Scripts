class Distancia(object):
	"""docstring for Distancias"""
	def __init__(self, numero):
		super(Distancia, self).__init__()
		self.numero = numero

	#Kms Hacia ---->
	def km_a_(self, hacia):
		return{
			"milla":"{:g}".format(self.numero*0.6214),
			"metro": "{:g}".format(self.numero*1000),
			"legua":"{:g}".format(self.numero/4.8280),
			"yarda":"{:g}".format(self.numero*1.0936100),
			"pie":"{:g}".format(self.numero*3.2808400),
			# "kms":"%g" %(self.numero),
		}.get(hacia,("{:g}".format(self.numero)))
	
	#Millas Hacia  ---->
	def milla_a_(self, hacia):
		return{
		"kms":"{:g}".format(self.numero/0.62137),
		"metro":"{:g}".format(self.numero/0.62137*1000),
		"legua":"{:g}".format(self.numero*0.2897),
		"yarda":"{:g}".format(self.numero*1760),
		"pie":"{:g}".format(self.numero*5280),
		}.get(hacia,("{:g}".format(self.numero)))

	# Metro Hacia ->
	def metro_a_(self,hacia):
		return{
		"kms":"{:g}".format(self.numero/1000),
		"milla":"{:g}".format(self.numero*0.6214/1000),
		"legua":"{:g}".format(self.numero/4.8280/1000),
		"yarda":"{:g}".format(self.numero*1.0936100/1000),
		"pie":"{:g}".format(self.numero*3.2808400/1000),
		}.get(hacia,("{:g}".format(self.numero)))


	#Legua Hacia ->
	def legua_a_(self,hacia):
		return{
		"kms":"{:g}".format(self.numero*4.8280),
		"milla":"{:g}".format(self.numero*3),
		"metro":"{:g}".format(self.numero*4.8280*1000),
		"yarda":"{:g}".format(self.numero*5.2799819),
		"pie":"{:g}".format(self.numero*15.8399939)
		}.get(hacia,("{:g}".format(self.numero)))

	#Yarda Hacia ->
	def yarda_a_(self,hacia):
		return{
		"kms":"{:g}".format(self.numero/1.0936),
		"milla":"{:g}".format(self.numero/1760),
		"metro":"{:g}".format(self.numero/0.0011),
		"legua":"{:g}".format(self.numero/5.28),
		"pie":"{:g}".format(self.numero/0.3333)
		}.get(hacia,("{:g}".format(self.numero)))

	#Pie Hacia ->
	def pie_a_(self,hacia):
				return{
		"kms":"{:g}".format(self.numero/3.2808/1000),
		"milla":"{:g}".format(self.numero/5280),
		"metro":"{:g}".format(self.numero/3.2808),
		"legua":"{:g}".format(self.numero/15.84),
		"yarda":"{:g}".format(self.numero*0.33333)
		}.get(hacia,("{:g}".format(self.numero)))

