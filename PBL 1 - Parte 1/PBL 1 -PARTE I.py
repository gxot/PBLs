import random
def gerar_lista_aleatoria(tamanho):
    numeros=[]
    for i in range (tamanho):
        numeros_aleatorios=random.randint(0,100)
        numeros.append(numeros_aleatorios)
    return numeros
tamanho_lista = input("Digite o tamanho da lista: ")
tamanho_lista = int(tamanho_lista)
numeros = gerar_lista_aleatoria(tamanho_lista)
for numero in numeros:
    if numero %2 == 0:
        print(numero, "É par")
    elif numero %3 == 0:
        print(numero,"Múltiplo de 3")
    else:
        print("É impar")