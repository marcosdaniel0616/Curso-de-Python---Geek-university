"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à teoria dos conjuntos
da matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre conjuntos (Set) e Mapas (Dicionários) em python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem valor;
# Definindo um conjunto

# Forma 1
s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erros
# e não fará parte do conjunto

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de náo termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# dicionários não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

"""

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em sets

s = {1, 'B', True, 34, 22, 44}
print(s)
print(type(s))

# Podemos iterar em um Set normalmente
for valor in s:
    print(valor)