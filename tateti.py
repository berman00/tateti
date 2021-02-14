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


	def __str__(self):
		'''
		Devuelve el tablero actual
		'''

		s = '\n'
		for fila in range(3):
			s = s + "\t| %s  %s  %s |" % tuple(self.tablero[fila*3:fila*3+3]) + '\n'
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


	def movimiento(self, ficha, fila, columna=None):
		'''
		Define el carácter de una pieza del tablero.
		Si se pasa solo el parametro fila, es como las teclas
		de un teléfono.
		Si se pasa fila y columna, es como las coordenadas de una
		celda de una matriz.
		'''

		if ficha not in [NADA, X, O]:
			raise ValueError("'ficha' debe ser NADA, X o O")
		
		if columna == None:
			if fila > 9 or fila < 1:
				raise ValueError("'fila' debe estar entre 1 y 9")
			
			self.tablero[fila-1] = ficha

		else:
			if columna > 3 or columna < 1:
				raise ValueError("'columna' debe estar entre 1 y 3")
			if fila > 3 or fila < 1:
				raise ValueError("'fila' debe estar entre 1 y 3")

			self.tablero[ (fila-1)*3 + columna -1] = ficha


	def reiniciar(self):
		'''
		Reinicia el tablero
		'''

		self.tablero  = [
			NADA, NADA, NADA,
			NADA, NADA, NADA,
			NADA, NADA, NADA
		]

	
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

		if ficha not in [NADA, X, O]:
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


	def tableroLleno(self):
		'''
		Devuelve True si el tablero está lleno
		'''

		for celda in self.tablero:
			if celda == NADA:
				return False
		return True


	def estado(self):
		'''
		Devuelve el estado actual del tablero
		MOV si hay movimientos
		GANA_X si ganó X
		GANA_O si ganó O
		EMPATE si hay un empate
		'''

		if self.gano(X):
			return GANA_X
		elif self.gano(O):
			return GANA_O
		elif self.tableroLleno():
			return EMPATE
		else:
			return MOV
