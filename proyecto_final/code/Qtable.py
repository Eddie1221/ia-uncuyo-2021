import json

#DEFINICIÓN DE LOS ESTADOS

#si hay peligro inmediato en las 4 direcciones
#C = Cuerpo, P = Pared, N = nada
dangerLEFT = [0,1]
dangerRIGHT = [0,1]
dangerUP = [0,1]
dangerDOWN = [0,1]

#Si la fruta esta a la izquierda o derecha de la cabeza de la serpiente, o se encuentra en la misma posición respecto al eje x
FrutaHorizontal = ["L", "R", "="]

#Si la fruta esta arriba o abajo de la cabeza de la serpiente, o se encuentra en la misma posición respecto al eje y
FrutaHVertical = ["U", "D", "="]

#Dirección de la serpiente
Direccion = ["L", "R", "U", "D"]

#Fruta adyacente
FrutaAdyacente = ["L", "R", "U", "D", "-"]

tabla={}

for a in FrutaHorizontal:
    for b in FrutaHVertical:
        for c in dangerLEFT:
            for d in dangerRIGHT:
                for e in dangerUP:
                    for f in dangerDOWN:
                        for g in Direccion:
                            for h in FrutaAdyacente:
                                tabla[str((a,b,c,d,e,f,g,h))] = [0,0,0,0]
                        
with open("qvalues.json", "w") as f:
	json.dump(tabla, f)