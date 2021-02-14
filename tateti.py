'''
Programa para jugar al tateti

Valentin Berman   13/02/20
'''

# Constantes

NADA = '-'
X = 'x'
O = 'o'




class Tateti():
	'''
	Clase que define un tablero de tateti
	'''

	posGanadoras = (
		(0,1,2),
		(3,4,5),
		(6,7,8),
		(0,3,6),
		(1,4,5),
		(2,5,8),
		(0,4,8),
		(2,4,6),

	)

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


	def jugar(self, tipo, fila, columna=None):
		'''
		Define el caracter de una pieza del tablero.
		Si se pasa solo el parametro fila, es como las teclas
		de un teléfono.
		Si se pasa fila y columna, es como las coordenadas de una
		celda de una matriz.
		'''
		if tipo not in [NADA, X, O]:
			raise ValueError("'tipo' debe ser NADA, X o O")
		
		if columna == None:
			if fila > 9 or fila < 1:
				raise ValueError("'fila' debe estar entre 1 y 9")
			
			self.tablero[fila-1] = tipo

		else:
			if columna > 3 or columna < 1:
				raise ValueError("'columna' debe estar entre 1 y 3")
			if fila > 3 or fila < 1:
				raise ValueError("'fila' debe estar entre 1 y 3")

			self.tablero[ (fila-1)*3 + columna -1] = tipo




# Prueba
x = Tateti()
x.jugar(X,1,1)
x.jugar(X, 5)
x.ver()