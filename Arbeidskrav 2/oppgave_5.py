import math

a = int(input('side a: '))
b = int(input('side b: '))

# regne ut side c for den rettvinklet trekanten
c = math.sqrt(a**2 + b**2)

areal_trekant = a*b/2

# regne ut halvparten av arealet
areal_sirkel = (math.pi * (a/2)**2) / 2
omkrets_sirkel = math.pi * a/2

# regner ut resultat og runder av til 2 desimaler
areal_total = round(areal_trekant + areal_sirkel, 2)
omkrets_total = round(omkrets_sirkel + b + c, 2)

# printe ut resultatet
print(f'Omkretsen av figuren er: {omkrets_total} enheter, og arealet er {areal_total} enheter.')