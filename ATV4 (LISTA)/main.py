"""
Uma administradora de condomínios está analisando o consumo de água de seus clientes. 
Ajude a administradora desenvolvendo um algoritmo que receba a quantidade de moradores (N) de um determinado condomínio, 
leia as N leituras de relógio de consumo de água, e por fim, 
apesente a média de consumo e a quantidade de condôminos que ficaram acima ou igual a média.
"""

def getConsumoCliente(num_cliente: int) -> int:
    """Obtenha o consumo de água do determinado cliente."""
    consumo = int(input(f'Qual foi o consumo de água do cliente {num_cliente}?\n>>> '))
    return consumo

def startLeituras(num_leituras: int) -> list[int]:
    """Começe a rotina de leitura de água."""
    leitura_list = []
    for i in range(0, num_leituras):
        leitura = getConsumoCliente(i+1)
        leitura_list.append(leitura)
    return leitura_list

def calcMediaLeituras(list_leituras: list[int]) -> float:
    """Calcule à media de todas as leituras."""
    soma = 0
    for leitura in list_leituras:
        soma += leitura
    return soma / len(list_leituras)

def findLeiturasAltas(list_leituras: list[int], media: int) -> int:
    """Descubra quantas leituras acima da média existe."""
    leituras_acima = 0
    for leitura in list_leituras:
        if leitura > media:
            leituras_acima += 1
    return leituras_acima

def main():
    quantidade_leituras = int(input('Quantas leituras serão feitas?\n>>> '))
    todas_leituras = startLeituras(quantidade_leituras)
    media_leituras = calcMediaLeituras(todas_leituras)
    acima_leituras = findLeiturasAltas(todas_leituras, media_leituras)

    print( '\n'
        + f'Media = {media_leituras}\n'
        + f'Acima = {acima_leituras}')

if __name__ == "__main__":
    main()