'''
programa que almacene la cadena de caracteres contraseña
'''

password = 'contraseña'

password_del_usuario = input('Introduzca la contraseña: ')
password_del_usuario = password_del_usuario.lower()

if password == password_del_usuario:
    print('Correcto')
else:
    print('Va a ser que no')