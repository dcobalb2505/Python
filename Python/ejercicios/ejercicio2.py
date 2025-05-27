parcial1 = float(input("Introduce la nota del primer parcial: "))
parcial2 = float(input("Introduce la nota del segundo parcial: "))
parcial3 = float(input("Introduce la nota del tercer parcial: "))
examen = float(input("Introduce la nota del examen final: "))
trabajo = float(input("Introduce la nota del trabajo final: "))
nota = ((parcial1 + parcial2 + parcial3) /3 )*0.55+0.3*examen+0.15*trabajo
print("La nota final es: %.2f" % nota)

