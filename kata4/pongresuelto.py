import  pygame , sys , random

def  ball_animation ():
	global  ball_speed_x , ball_speed_y
	
	pelota . x  + =  velocidad_bola_x
	pelota . y  + =  velocidad_bola_y

	Si  pelota . top  <=  0  o  bola . bottom  > =  screen_height :
		ball_speed_y  * =  - 1
	Si  pelota . izquierda  <=  0  o  bola . derecha  > =  ancho_pantalla :
		ball_start ()

	Si  pelota . colisionar ( jugador ) o  pelota . colisionar ( oponente ):
		ball_speed_x  * =  - 1

def  player_animation ():
	jugador . y  + =  velocidad_jugador

	Si  el jugador . arriba  <=  0 :
		jugador . arriba  =  0
	Si  el jugador . bottom  > =  screen_height :
		jugador . bottom  =  screen_height

def  oponent_ai ():
	Si  oponente . arriba  <  pelota . y :
		oponente . y  + =  velocidad del oponente
	Si  oponente . fondo  >  pelota . y :
		oponente . y  - =  velocidad del oponente

	Si  oponente . arriba  <=  0 :
		oponente . arriba  =  0
	Si  oponente . bottom  > =  screen_height :
		oponente . bottom  =  screen_height

def  ball_start ():
	global  ball_speed_x , ball_speed_y

	pelota . centro  = ( ancho_pantalla / 2 , altura_pantalla / 2 )
	ball_speed_y  * =  aleatorio . elección (( 1 , - 1 ))
	ball_speed_x  * =  aleatorio . elección (( 1 , - 1 ))

# Configuración general
pygame . init ()
reloj  =  pygame . tiempo . Reloj ()

# Ventana principal
ancho_pantalla  =  1280
screen_height  =  960
pantalla  =  pygame . mostrar . set_mode (( screen_width , screen_height ))
pygame . mostrar . set_caption ( 'Pong' )

# Colores
gris claro  = ( 200 , 200 , 200 )
bg_color  =  pygame . Color ( 'gris12' )

# Rectángulos de juego
pelota  =  pygame . Rect ( screen_width  /  2  -  15 , screen_height  /  2  -  15 , 30 , 30 )
jugador  =  pygame . Rect ( ancho_pantalla  -  20 , altura_pantalla  /  2  -  70 , 10 , 140 )
oponente  =  pygame . Rect ( 10 , altura_pantalla  /  2  -  70 , 10 , 140 )

# Variables del juego
ball_speed_x  =  7  *  aleatorio . elección (( 1 , - 1 ))
ball_speed_y  =  7  *  aleatorio . elección (( 1 , - 1 ))
player_speed  =  0
oponent_speed  =  7

mientras  cierto :
	para  evento  en  pygame . evento . obtener ():
		si  evento . tipo  ==  pygame . QUIT :
			pygame . salir ()
			sys . salida ()
		si  evento . tipo  ==  pygame . CLAVE :
			si  evento . clave  ==  pygame . K_UP :
				player_speed  - =  6
			si  evento . clave  ==  pygame . K_DOWN :
				player_speed  + =  6
		si  evento . tipo  ==  pygame . KEYUP :
			si  evento . clave  ==  pygame . K_UP :
				player_speed  + =  6
			si  evento . clave  ==  pygame . K_DOWN :
				player_speed  - =  6
	
	# Lógica del juego
	ball_animation ()
	player_animation ()
	oponent_ai ()

	# Visuales 
	la pantalla . relleno ( bg_color )
	pygame . dibujar . rect ( pantalla , gris claro , jugador )
	pygame . dibujar . rect ( pantalla , gris claro , oponente )
	pygame . dibujar . elipse ( pantalla , gris claro , bola )
	pygame . dibujar . aaline ( screen , light_grey , ( screen_width  /  2 , 0 ), ( screen_width  /  2 , screen_height ))

	pygame . mostrar . voltear ()
	reloj . garrapata ( 60 )