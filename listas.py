"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem DINÂMICO
e também de podermos colocar QUALQUER tipo de dado.

linguagens C/Java: Arrays
    - Possuem tamanhos e tipo de dado fixo;
    Ou seja, nessas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter SEMPRE, no máximo, 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em pythons são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 13
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com append, nós só conseguimos adicionar um elemento por vez
# lista1.append(12, 34, 56) # erro

lista1.append([8, 3, 1])  # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas
lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# forma 1
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)

# forma 2
print(lista1[::-1])
print(lista2[::-1])

# copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista2))


# Podemos remover facilmente o último elemento da lista
# OBS: O pop não só remove o último elemento como também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita deste índice, serão deslocados para a esquerda.
# OBS2: Se não houver elemento no índice informado, teremos o erro index error.

lista5.pop(2)
print(lista5)

# Podemos facilmente remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova *= 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo um 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre eles.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)
# Abaixo estamos falando: pega a lista 6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1,2,3], 458394858]
print(lista6)
print(type(lista6))

# Iterando sobre listas


# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista4:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#           0         1         2        3
cores = ['Verde', 'Amarelo', 'Azul', 'Branco']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# fazer acesso aos elementos de forma indexada reversa

# para entender melhor o índice negativo, pense no índice como um círculo, onde
# o final de um elemento está ligado ao início da lista
print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # Verde
# print(cores[-5]) # erro, pois não existe o índice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(f'{indice} : {cor}')

# listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)


"""

# Outros métodos não tão importantes mas também úteis

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

# print(numeros.index(19)) # Gera valueError
# OBS: caso não tenha este elemento na lista, será apresentado erro valueError

# OBS: Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2

# OBS: caso não tenha este elemento na lista, será apresentado erro valueError
# print(numeros.index(5, 4)) # buscando a partir do índice 4

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6)) # Buscar o índice do valor 8, entre 3 e 6
