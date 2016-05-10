import math 
def calculoAreaTriangulo(a,b,c):
	s=((a+b+c)/2)
	aux=(s*(s-a)*(s-b)*(s-c))
	aux1=math.sqrt(aux)
	return aux1

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

#Funciones de un pentagono regular todos sus lados e angulos iguales
def calculoPerimetroPentagono(lado):
	return lado*5
def calculoAreaPentagono(lado, radio):
	ca=lado/2
	n=((radio*radio)-(ca*ca))
	apotema= math.sqrt(n)
	per=lado*5
	area=((per*apotema)/2)
	return area


r=int(input("Cuantos lados desea ingresar \n"))
if ((r==1) or (r==2)):
	print("Con estos numeros de lados no se puede formar una figura geometrica\n")
if (r>5):
	print("Se exedio con el numero de lados se permite unicamente 5 lados \n")
if (r==3):
	print("Usted puede formar un triangulo\n")
	a=int(input("Ingrese el primer lado del triangulo\n"))
	b=int(input("Ingrese el segundo lado del triangulo\n"))
	c=int(input("Ingrese el tercer lado del triangulo\n"))
	aux=calculoAreaTriangulo(a,b,c)
	print (" EL AREA DEL TRIANGULO ES: "+str(aux))
	aux1=calculoPerimetroTriangulo(a,b,c)
	print (" EL PERIMETRO DEL TRIANGULO ES: "+str(aux1))
if (r==4):
	x=int(input("Puede formar: \n1-Cudrado \n2-Rectangulo \n"))
	if(x==1):		 
		l=int(input("Ingrese un lado del cuadrado\n"))
		aux2=calculoAreaCuadrado(l)
		aux3=calculoPerimetroCuadrado(l)
		print (" EL AREA DEL CUADRADO ES: "+str(aux2)) 
		print (" EL PERIMETRO DEL CUADRADO ES: "+str(aux3)) 
	if(x==2):
		b=int(input("Ingrese la base del rectangulo\n"))
		h=int(input("Ingrese la altura del rectangulo\n"))
		aux4=calculoAreaRectangulo(b,h)
		aux5=calculoPerimetroRectangulo(b,h)
		print (" EL AREA DEL RECTANGULO ES: "+str(aux4)) 
		print (" EL PERIMETRO DEL RECTANGULO ES: "+str(aux5)) 
	if(x>2):
		print("No existe la opcion \n")
if(r==5):
	print (" Puede formar un pentagono regular ")
	lado=int(input("Ingrese el lado del pentago\n"))
	radio=int(input("Ingrese el radio del pentagono\n"))
	aux6=calculoAreaPentagono(lado,radio)
	aux7=calculoPerimetroPentagono(lado)
	print (" EL AREA DEL PENTAGONO ES: "+str(aux6)) 
	print (" EL PERIMETRO DEL PENTAGONO ES: "+str(aux7)) 

		





