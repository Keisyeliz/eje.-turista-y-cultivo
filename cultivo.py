papaInt = 0
yucaInt = 0
zanahoriaInt = 0

tipo_cultivoInt = int(input('<<<MENÚ DE OPCIONEs>>>\n\n1. papa\n2. yuca\n3. zanahoria\n ->'))

if tipo_cultivoInt ==1:
    for  i in range (3):
        ltsInt = int(input('Con cuantos lts regaste -> '))
        papaInt += ltsInt
    print('Los litros consumidos esta semana para la riega de papa fueron: ',papaInt)        

if tipo_cultivoInt ==2:
     for  i in range (2):
        ltsInt = int(input('Con lts cuantos regaste -> '))
        yucaInt += ltsInt
     print('Los litros consumidos esta semana para la riega de la yuca fueron: ',yucaInt)   

if tipo_cultivoInt == 3:
    for  i in range (2):
        ltsInt = int(input('Con cuantos lts regaste -> '))
        zanahoriaInt += ltsInt
    print('Los litros consumidos esta semana para la riega de zanahoria fueron: ',zanahoriaInt)   
