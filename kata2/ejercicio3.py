'''
programa para salas de juego y saber si es mayor de edad
si es menor de 4 años gratis, entre 4 y 18 5€, si es mayor 
10€
'''

edad = input('Introduce tu edad: ')
edad = int(edad)

if edad < 4:
    print('El precio es GRATUITO.')
elif edad >= 4 and edad <= 18:
    print('El precio es 5€.')
else:
    print('El precio es 10€.')