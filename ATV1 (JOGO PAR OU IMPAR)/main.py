import random, os
from pessoa import Pessoa

# TODO:   
#         [ ] 1) Limpar o codigo em geral.

def getplayerchoice(jogador, cpu):
	choice = 0
	while choice not in [1, 2]:
		choice = int(input("Você quer PAR ou IMPAR? \n1: IMPAR;\n2: PAR\n>>> "))

		if choice == 1:
			print("Você escolheu IMPAR.\n")
			jogador.setWincon(1)
			cpu.setWincon(2)
		elif choice == 2:
			print("Você escolheu PAR.\n")
			jogador.setWincon(2)
			cpu.setWincon(1)
		else:
			print("Escolha uma opção válida.\n")

def startgame():
	jogador = Pessoa()
	cpu = Pessoa()

	while (jogador.getWins() < 3) and (cpu.getWins() < 3):

		getplayerchoice(jogador, cpu)
		j_num = ""
		while j_num not in [0, 1, 2, 3, 4, 5]:
			j_num = int(input(f"Por favor escolha um dos seguintes números para jogar número para jogar: 0 | 1 | 2 | 3 | 4 | 5 \n>>> "))
		jogador.setChoice(j_num)
		print(f"Você escolheu {jogador.getChoice()}")

		random.seed()
		cpu.setChoice(random.randint(0,5))
		print(f"Seu inimigo escolheu {cpu.getChoice()}!")

		soma = jogador.getChoice() + cpu.getChoice()

		if soma % 2 == 0:
			checkwinner(jogador, cpu, 2)
		else:
			checkwinner(jogador, cpu, 1)

		print(f"PLACAR:\n    Jogador: {jogador.getWins()}\n    CPU: {cpu.getWins()}\n")
	print("FIM DE JOGO.")
	retry = 0
	while retry not in [1, 2]:
		retry = int(input("Gostaria de tentar novamente?\n1: Sim;\n2:Não\n>>> "))
	if retry == 1:
		startgame()
	else:
		print("Até mais.")


def checkwinner(p1, p2, result):
	if p1.getWincon() == result:
		print("Você ganhou!\n")
		p1.increaseWins()
	else:
		print("Você perdeu...\n")
		p2.increaseWins()

if __name__ == '__main__':
	startgame()