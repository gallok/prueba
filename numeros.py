#!/usr/bin/env python
# -*- coding: utf-8 -*-- coding: utf-8 -*-
print "Cálculo de superficies:"
print """ 
1.-Cuadrados
2.-Triángulos
3.-Círculos
4.-Salir"""
i = 0
while i >=0 :
	option = int(raw_input("Elija opción (1 - 4) "))
	i = i + 1   
	if option == 1:
		lado = int(raw_input("Introduzca el lado"))
		area = lado * lado
		print "El area del cuadrado es: ", area
	elif option == 2:
		base = int(raw_input("Introduzca la base"))
		altura = int(raw_input("Introduzca la altura"))
		area = (base * altura) / 2
		print "El area del triangulo es: ", area
	elif option == 3:
		pi = 3.1416
		radio = int(raw_input("Introduzca el radio"))
		area = pi * (radio ** radio)
		print "El area del circulo es: ", area
	elif option == 4:
		break
	else:
		print "Debes introducir un numero entre 1 y 4"
