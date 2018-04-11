#1era evaluacion 2013-2014
#Tema 4
from random import*

n=int(input('Cuantos jugadores va a inscribir?: '))
registrados=[[0]*2 for i in range(n)]
equipo1=[0]*11
equipo2=[0]*11
for jugador in range(n):
	v=0
	while v!=1:
		a=int(input('Ingrese la habilidad del jugador: '))
		if a>4 or a<1:
			print('Habilidad no valida')
		else:
			registrados[jugador][0]=a
			v=1

arquero=0
defensa=0
mediocampo=0
delantero=0
for i in range(11):
	v=0
	while v!=1:
		a=randint(0,n-1)
		if registrados[a][1]==0:
			b=registrados[a][0]
			if b==1 and arquero<1:
				arquero=arquero+1
				v=1
				registrados[a][1]=1
				equipo1[i]=a
			elif b==1 and defensa<4:
				defensa=defensa+1
				v=1
				registrados[a][1]=1
				equipo1[i]=a
			elif b==3 and mediocampo<2:
				mediocampo=mediocampo+1
				v=1
				registrados[a][1]=1
				equipo1[i]=a
			elif b==4 and delantero<4:
				delantero=delantero+1
				v=1
				registrados[a][1]=1
				equipo1[i]=a

arquero=0
defensa=0
mediocampo=0
delantero=0
for i in range(11):
	v=0
	while v!=1:
		a=randint(0,n-1)
		if registrados[a][1]==0:
			b=registrados[a][0]
			if b==1 and arquero<1:
				arquero=arquero+1
				v=1
				registrados[a][1]=2
				equipo2[i]=a
			elif b==1 and defensa<4:
				defensa=defensa+1
				v=1
				registrados[a][1]=2
				equipo2[i]=a
			elif b==3 and mediocampo<2:
				mediocampo=mediocampo+1
				v=1
				registrados[a][1]=2
				equipo2[i]=a
			elif b==4 and delantero<4:
				delantero=delantero+1
				v=1
				registrados[a][1]=2
				equipo2[i]=a

print(equipo1)
print(equipo2)
