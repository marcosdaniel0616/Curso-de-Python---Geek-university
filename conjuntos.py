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
"""

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
