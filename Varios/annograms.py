#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Implementar la funcion annograms que usa el archivo WORD.LST 
#para devolver anagramas de la palabra dada en el parametro word

def annograms(word):
	try:
		words = [w.rstrip('\n') for w in open('resources/WORDS.LST')]
		wordLower=word.lower()
		setA=set([(i,wordLower.count(i)) for i in wordLower])
		result=[]
		for i in words:
			if i != wordLower:
				if len(i)==len(wordLower):
					setB=set([(z,i.count(z)) for z in i])
					if setB==setA:
						result.append(i)
	except:
		return "Un error en el parametro de ingreso"

	return "Anagramas de la palabra -{}- son {}".format(wordLower,result)

if __name__ == "__main__":
	print annograms("train")
	print '--'
	print annograms('drive')
	print '--'
	print annograms('python')	