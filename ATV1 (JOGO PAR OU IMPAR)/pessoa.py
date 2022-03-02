# TODO:   (Copiado do main.py)
#         [ ] 1) Limpar o codigo em geral.

class Pessoa():
	def __init__(self):
		self.wins = 0

	def setWincon(self, wincon):
		self.wincon = wincon

	def getWincon(self):
		return self.wincon

	def setChoice(self, choice):
		self.choice = choice

	def getChoice(self):
		return self.choice

	def increaseWins(self):
		self.wins += 1

	def getWins(self):
		return self.wins