#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Implementar la funcion “thousands_with_commas” que toma un 
#integer y devuelve un string con el número con comas cada 3 dígitos.

def thousands_with_commas(i):
	try:
		i="{:,}".format(i)
	except:
		return "Error de parametro de ingreso"

	return i


if __name__ == '__main__':
	print thousands_with_commas(1234) == '1,234'
	assert thousands_with_commas(123456789) == '123,456,789'
	assert thousands_with_commas(12) == '12'