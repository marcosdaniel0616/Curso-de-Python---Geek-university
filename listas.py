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
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: pega a lista 6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)