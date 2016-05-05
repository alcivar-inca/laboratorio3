def creartxt():
	archi = open ('GUIA_2.txt', 'w')
	archi.close()
def grabartxt(nom, apel, num):
	archi = open ('GUIA_2.txt','a')
	archi.write("NOMBRE: ")
	archi.write(nom)
	archi.write("\n")
	archi.write("APELLIDO: ")
	archi.write(apel)
	archi.write("\n")
	archi.write("TELEFONO: ")
	archi.write(num)
	archi.write("\n")
	archi.close()
	

creartxt()

o = 1
while o <= 3:
	nom = input("NOMBRE: ")
	apel = input("APELLIDO: ")
	num = input("TELEFONO: ")
	grabartxt(nom, apel, num)
	o = o + 1

