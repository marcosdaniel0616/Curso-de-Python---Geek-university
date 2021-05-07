"""
Entendendo o *args

- O *args é um parâmetro, como qualquer outro, isso significa que você poderá chamar de qualquer coisa,
desde que comece com asterísco.

Exemplo:

*xis

Mas por convenção, utilizamos *args para definí-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos


def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4


print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))

print(soma_todos_numeros(4, 6, 9, 5))

# Entendendo o args


def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'Jolie'))
print(soma_todos_numeros('Angelina', 'Jolie', 1))
print(soma_todos_numeros('Angelina', 'Jolie', 2, 3))
print(soma_todos_numeros('Angelina', 'Jolie', 3, 4, 5, 6))

# Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo, Geek'
    else:
        return 'Eu não sei quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
print(verifica_info('Geek University'))
print(verifica_info('Geek', 'University'))
"""


