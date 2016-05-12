# PROGRAMA PARA CALCULAR EL AREA Y PERIMETRO DE FIGUARAS GEOMETRICAS
import math
import os
opc = 1
def calculoAreaTriangulo(a,b,c):
	s=((a+b+c)/2)
	aux= math.sqrt((s*(s-a)*(s-b)*(s-c)))
	return aux

def calculoPerimetroTriangulo(a,b,c):
	s= (a+b+c)
	return s

def calculoAreaCuadrado(l):
	return l*l

def calculoPerimetroCuadrado(l):
	return l*4

def calculoAreaRectangulo(b,h):
	return b*h

def calculoPerimetroRectangulo(b,h):
	return ((2*b) + (2*h))

#Funciones de un pentagono regular todos sus lados y angulos iguales
def calculoPerimetroPentagono(lado, numLados):
	return lado*numLados

def calculoAreaPoligono(lado, NumLados):
	angulo=360/NumLados
	apotema= lado/(2*(math.tan(math.radians(angulo/2))))
	area = lado*NumLados*apotema/2
	return area

while opc==1:
	os.system("cls")
	print("CALCULO DEL AREA Y PERIMETRO DE UN POLIGONO DADO SUS LADOS\n")
	r=int(input("Cuantos lados desea ingresar: "))

	if (r <= 2):
		print("NO se puede formar una figura geometrica con " + str(r) + " lados\n")
	if (r==3):
		print("Con " + str(r) + " lados se forma un triangulo\n")
		a=int(input("Ingrese el primer lado del triangulo: "))
		b=int(input("Ingrese el segundo lado del triangulo: "))
		c=int(input("Ingrese el tercer lado del triangulo: "))
		print (" EL AREA DEL TRIANGULO ES: "+ str (calculoAreaTriangulo(a,b,c)))
		print (" EL PERIMETRO DEL TRIANGULO ES: "+str(calculoPerimetroTriangulo(a,b,c)))
	if (r==4):
		x=int(input("Con " + str(r) + " lados puede formar: \n1-Cudrado \n2-Rectangulo \nEscoja una opcion: "))
		if(x==1):		 
			l=int(input("Ingrese un lado del cuadrado: "))
			print (" EL AREA DEL CUADRADO ES: "+str(calculoAreaCuadrado(l))) 
			print (" EL PERIMETRO DEL CUADRADO ES: "+str(calculoPerimetroCuadrado(l))) 
		elif(x==2):
			b=int(input("Ingrese la base del rectangulo: "))
			h=int(input("Ingrese la altura del rectangulo: "))
			print (" EL AREA DEL RECTANGULO ES: "+str(calculoAreaRectangulo(b,h))) 
			print (" EL PERIMETRO DEL RECTANGULO ES: "+str(calculoPerimetroRectangulo(b,h))) 
		else:
			print("No existe la opcion \n")
	if(r>=5):
		print (" Puede formar un poligono regular ")
		lado=int(input("Ingrese el lado del poligono regular: "))
		print (" EL AREA DEL POLIGONO ES: "+str(calculoAreaPoligono(lado,r))) 
		print (" EL PERIMETRO DEL POLIGONO ES: "+str(calculoPerimetroPentagono(lado, r)))
	opc=int(input("Para CONTINUAR presione 1. \nPara SALIR presione 2. : "))
