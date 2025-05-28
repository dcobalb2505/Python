nombre = input("Dime tu nombre: ")
apellido1= input("Dime tu primer apellido: ")
apellido2 = input("Dime el segundo apellido: ")
inicial = nombre[0]
inicial += apellido1[0]
inicial += apellido2[0]
inicial = inicial.upper()
print("Laas iniciales son: ", inicial)