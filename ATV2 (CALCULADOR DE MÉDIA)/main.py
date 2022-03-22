# Primeiramente sinto a necessidade de expressar meu descontento com à limitação que eu só possa utilizar um arquivo, mas enfim...


# WIP, NÃO É PARA ENTEGRAR.
def media(n1, n2):
	return (n1+n2)/2

def maior(n1, n2):
	if n1 > n2:
		return n1
	return n2

def aprovado(media):
	if media >= 6:
		return True
	return False

P1, P2 = (map(float, input("Digite as duas notas referentes à P1 e P2, separada por um espaço. (EX: 10 7)\n>>> ").split(" ")))
print(P1, P2)

if media(P1, P2) < 6:
	SUB = float(input("Você não foi aprovado pela média. Por favor insira a nota da sua prova substitutiva.\n>>> "))
	print(SUB)

	# if maior(SUB, P1):
	# 	NP1 = SUB
	# 	NP2 = P2
	# elif maior(SUB, P2):
	# 	NP1 = P1
	# 	NP2 = SUB

	P1, P2 = (map(maior, [SUB, SUB], [P1, P2]))
	print(P1, P2)

	if media(P1, P2) < 6:
		EXAME = float(input("Você ainda não foi aprovado com a SUB. Por favor insira a nota do exame.\n>>> "))

		if media(EXAME, media(P1, P2)) < 6:
			print("Reprovado.")
else:
	print("Aprovado")
