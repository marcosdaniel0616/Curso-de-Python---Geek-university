"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError


def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))  # por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro número, e será calculado o
# quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro número e o segundo ao parâmetro potência,
# então, será calculado esta potência.

print(exponencial())

# OBS: Em funções Python, os parâmetros com valores padrão DEVEM sempre estar ao final da declaração

# ERRO!
def teste(num=2, potencia):
    return num ** potencia

# Correto!
def teste(potencia, num=2):
    return num ** potencia

# Outras exemplos

def soma(num1=5, num2=3):
    return num1 + num2


print(soma(4, 3))
print(soma(4))
print(soma())

# Exemplo mais complexo


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo, intrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    else:
        return f'Olá {nome}!'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao(nome='Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por que utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretors;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como valores default para parâmetros?

- Quaisquer tipos de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá prefência naquele local.

def diz_oi():
    prof = 'Geek'  # Variável local
    return f'Ola {prof}'


print(diz_oi())

print(prof)  # NameError

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    total = total + 1  # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido
    # inicializada)
    return total


print(incrementa())

# Atenção com variáveis globais (Se puder evitar, evite!)

total = 0


def incrementa():
    global total  # Avisando que iremos utilizar a variável global

    total = total + 1  # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido
    # inicializada)
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções declaradas dentro de funções, e também tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())

print(dentro())  # NameError!

"""


