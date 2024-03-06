
total_distancia = 0
nombreStr = input("Ingrese su nombre: ")
numero_etapas = int(input("Ingresa el numero de etapas: "))

 
for etapas in range(numero_etapas):
    distanciaInt = int(input("ingrese la distancia de las etapas: "))
    total_distancia += distanciaInt
    
print('Nombre del turista: ',nombreStr)   
print("la distancia total es: ", total_distancia,'km')
print('el numero de etapas es','No. ', numero_etapas)