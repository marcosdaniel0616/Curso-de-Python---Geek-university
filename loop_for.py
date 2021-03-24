"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek university'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
for numero in range(1, 10):
range(valor_inicial, valor_final)

OBS: O valor final não é inclusivo.
1
2
3
4
5
6
7
8
9
10 - Não
    print(numero)

for indice, letra in enumerate(nome):
    print(nome[índice])

for _, letra in enumerate(nome):
    print(indice)
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando o underline(_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # temos que transformar em uma lista


for valor in enumerate(nome):
    print(valor)
"""

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num
print(f'A soma é {soma}')