horaPartida = int(input("Hora de salida: "))
minPartida = int(input("Minutos de salida: "))
segPartida = int(input("Segundos de salida: "))
segViaje = int(input("Tiempo que  se tarda en segundos: "))
#Convierto todo en segundos
seginicial = horaPartida *3600 + minPartida * 60 +segPartida;
seginicial += segViaje;
horallegada = seginicial //3600;
minllegada = (seginicial%3600)//60;
segllegada = (seginicial %3600 )%60;
print("Hora de llegada")
print(horallegada,":",minllegada,":", segllegada)
