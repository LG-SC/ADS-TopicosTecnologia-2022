# TODO:   (Copiado do main.py)
#         [ ] 1) Implementar metódo resetPlayer() e permitir o jogador a conduzir uma novar partida sem ter que 
#              rodar o programa novamente;
#         [ ] 2) Limpar o codigo em geral.

class Pessoa():
	def __init__(self):
		self.wins = 0

	def setWincon(self, wincon):
		self.wincon = wincon

	def getWincon(self):
		return self.wincon

	def resetPlayer(self, wincon): # Inutilizado (por momento).
		setWincon(wincon)
		self.wins = 0

	def setChoice(self, choice):
		self.choice = choice

	def getChoice(self):
		return self.choice

	def increaseWins(self):
		self.wins += 1

	def getWins(self):
		return self.wins