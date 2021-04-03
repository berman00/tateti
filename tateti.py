'''
Programa para jugar al tateti

Valentin Berman   13/02/20
'''

# Constantes

NADA = '-'
X = 'x'
O = 'o'
MOV = 'hay movimientos'
GANA_X = 'ganó X'
GANA_O = 'ganó O'
EMPATE = 'empate'

# Clases

class Tateti():
	'''
	Clase que define un tablero de tateti
	'''

	def __init__(self):
		
		self.tablero  = [
			NADA, NADA, NADA,	# | 0  1  2 |
			NADA, NADA, NADA,	# | 3  4  5 |
			NADA, NADA, NADA	# | 6  7  8 |
		]

		self.turno = 0

		self.movDisp = [1,2,3,4,5,6,7,8,9]


	def __str__(self):
		'''
		Devuelve el tablero actual
		'''

		s = '\n\tTABLERO:\n\n'
		for fila in range(3):
			s = s + "\t| %s  %s  %s |" % tuple(self.tablero[fila*3:fila*3+3]) + '\n'
		s = s + "\n\tTURNO: %d\n" % self.turno
		return s


	def ver(self):
		'''
		Imprime en pantalla el tablero actual
		Equivalente a print(Tateti)
		'''

		print('')
		for fila in range(3):
			print("\t| %s  %s  %s |" % tuple(self.tablero[fila*3:fila*3+3]))
		print('')


	def verTurno(self):

		print("\n\tTURNO: %d\n" % self.turno)


	def preparar(self, ficha, lpos):
		'''
		'lpos' es una lista de posiciones que se cambian al valor de 'ficha'.
		Cambia el turno del tablero, por lo tanto se recomiendo tener en
		cuenta que en el primer turno se juega X, el segundo O, etc.
		Devuelve el turno actual
		Las posiciones son:
		| 1  2  3 |
		| 4  5  6 |
		| 7  8  9 |
		'''

		if ficha not in (X, O, NADA):
			raise ValueError("'ficha' debe ser X, O o NADA")
		
		if type(lpos) is not list:
			raise ValueError("'lpos' debe ser una lista")
		
		for pos in lpos:
			if pos > 9 or pos < 1:
				raise ValueError("los elementos de 'lpos' deben estar entre 1 y 9")
						
			self.tablero[pos-1] = ficha

			cuent = 0
			self.movDisp = [1,2,3,4,5,6,7,8,9]
			for indice, celda in enumerate(self.tablero):
				if celda in [X,O]:
					cuent += 1
					self.movDisp.remove(indice+1)
			self.turno = cuent

		return self.movDisp

	
	def jugar(self, pos, ficha='auto'):
		'''
		Juega en la posición 'pos'. Selecciona la ficha
		correspondiente automáticamente, o se puede
		sobreescribir con 'ficha'.
		Devuelve el turno actual.
		Las posiciones son:
		| 1  2  3 |
		| 4  5  6 |
		| 7  8  9 |
		'''

		if pos > 9 or pos < 1:
			raise ValueError("'pos' debe estar entre 1 y 9")

		if pos not in self.movDisp:
			raise ValueError("'%d' no es un movimiento disponible" % pos)

		if ficha not in (X,O, 'auto'):
			raise ValueError("'ficha' debe ser X, O o 'auto'")

		if ficha == 'auto':
			if self.turno % 2 == 0:
				ficha = X
			else:
				ficha = O
		
		self.tablero[pos-1] = ficha
		self.turno += 1
		self.movDisp.remove(pos)

		return self.movDisp


	def reiniciar(self):
		'''
		Reinicia el tablero
		'''

		self.tablero  = [
			NADA, NADA, NADA,
			NADA, NADA, NADA,
			NADA, NADA, NADA
		]

		self.turno = 0

		self.movDisp = [1,2,3,4,5,6,7,8,9]
	

	def gano(self, ficha):
		'''
		Devuelve True si 'ficha' ganó, si no devuelve False
		'''

		posGanadoras = (
			(0,1,2),
			(3,4,5),
			(6,7,8),
			(0,3,6),
			(1,4,7),
			(2,5,8),
			(0,4,8),
			(2,4,6),
		)

		if ficha not in (NADA, X, O):
			raise ValueError("'ficha' debe ser NADA, X o O")		

		posConFicha=[]
		for indice, celda in enumerate(self.tablero):
			if celda == ficha:
				posConFicha.append(indice)

		for pos in posGanadoras:
			if pos[0] in posConFicha:
				if pos[1] in posConFicha:
					if pos[2] in posConFicha:
						return True
					else:
						continue
				else:
					continue
			else:
				continue
		return False


	def estado(self):
		'''
		Devuelve el estado actual del tablero
		MOV si hay movimientos
		GANA_X si ganó X
		GANA_O si ganó O
		EMPATE si hay un empate
		'''

		if   self.gano(X):
			return GANA_X
		elif self.gano(O):
			return GANA_O
		elif self.turno >= 9:
			return EMPATE
		else:
			return MOV


# Programa principal

if __name__ == '__main__':

	from random import choice
	from time import sleep

	# Funciones

	def prompt():
		return input('>>> ').lower()

	# Variables

	instrucciones = """
tateti		por Valentin Berman

Instrucciones:
q - salir
h - imprime este texto
[1-9] - selecciona una celda para jugar

Empieza usted, jugando con X
"""

	lComandos = ('h', 'q', '1', '2', '3', '4', '5', '6', '7', '8', '9')

	mensajeError = """Comando desconocido. Use 'h' para ver todo los comandos."""

	celdaOcupada = """Esa celda ya está ocupada, elija otra"""

	mensajeGanador = """Felicidades, usted ganó!!\nJugar de nuevo? (s/n)"""

	mensajeEmpate = """Empate!!\nJugar de nuevo? (s/n)"""

	mensajePerdedor = """Perdiste, que lástima!!\nJugar de nuevo? (s/n)"""

	# Programa
	
	print(instrucciones)
	ttt = Tateti()
	
	while True:   # Loop de todo el juego

		ttt.reiniciar()

		while True:   # Loop de turno

			comd = prompt()

			while comd not in lComandos:
				print(mensajeError)
				comd = prompt()

			if comd == 'q':   # Salir
				exit()

			elif comd == 'h':   # Ayuda
				print(instrucciones)

			elif comd in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):   # Juego

				# Turno Jugador:

				comd = int(comd)	# comd cambia de str a int !!!
				
				if comd not in ttt.movDisp:
					print(celdaOcupada)
					continue

				ttt.jugar(comd)
				ttt.ver()

				if ttt.estado() in (GANA_X,EMPATE):
					if ttt.estado() == GANA_X:
						print(mensajeGanador)
					else:
						print(mensajeEmpate)
					comd = prompt()
					while comd not in ('s','n','si','no'):
						print("Jugar de nuevo? ('si' o 's' para jugar, 'no' o 'n' para salir)")
						comd = prompt()
					if comd in ('n', 'no'):
						exit()
					else:
						print("Nueva ronda\n")
						break

				# Turno maquina:

				print("Es mi turno. Pensando", end='', flush=True)   # Espera un segundo para experiencia de usuario
				for _ in range(5):
					sleep(0.5)
					print('.',end='',flush=True)
				print()

				ttt.jugar(choice(ttt.movDisp))
				ttt.ver()

				if ttt.estado() == GANA_O:
					print(mensajePerdedor)
					comd = prompt()
					while comd not in ('s','n','si','no'):
						print("Jugar de nuevo? ('si' o 's' para jugar, 'no' o 'n' para salir)")
						comd = prompt()
					if comd in ('n', 'no'):
						exit()
					else:
						print("Nueva ronda\n")
						break
