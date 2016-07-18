class Almacenamiento(object):
	"""docstring for Almacenamiento"""
	def __init__(self, numero):
		super(Almacenamiento, self).__init__()
		self.numero = numero
		
	#Gbs Hacia ->
	def gb_a_(self, hacia):
		return{
		"Mbs":"{:g}".format(self.numero*1024),
		"Kbs":"{:g}".format(self.numero*1024*1024),
		"bytes":"{:g}".format(self.numero*1024*1024*1024)
		}.get(hacia,("{:g}".format(self.numero)))

	#Mbs Hacia ->
	def mb_a_(self, hacia):
		return{
		"Gbs":"{:g}".format(self.numero/1024),
		"Kbs":"{:g}".format(self.numero*1024),
		"bytes":"{:g}".format(self.numero*1024*1024)
		}.get(hacia,("{:g}".format(self.numero)))

	#Kbs Hacia ->
	def kbs_a_(self, hacia):
		return{
		"Gbs":"{:g}".format((self.numero/1024)/1024),
		"Mbs":"{:g}".format(self.numero/1024),
		"bytes":"{:g}".format(self.numero*1024*1024)
		}.get(hacia,("{:g}".format(self.numero)))


	#Bytes Hacia ->
	def bytes_a_(self, hacia):
		return{
		"Gbs":"{:g}".format(((self.numero/1024)/1024)/1024),
		"Mbs":"{:g}".format(((self.numero/1024)/1024)),
		"Kbs":"{:g}".format((self.numero/1024))
		}.get(hacia,("{:g}".format(self.numero)))
