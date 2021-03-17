"""
PEP 8 - Python Enhancement Proposal

São propostas de melhoria para a linguagem Python

Zen of Python

Import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - utilize Camel case para nome de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para identação! (NÃO use tab)

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports

- Imports devem ser sempre feitos em linhas separadas;

# Import Errado

import sys, os

# Import certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)
# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções

# Não faça:

funcao( algo [ 1 ]), { outro: 2 })

# faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = lista(indice)

# Não faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha
"""
import this
