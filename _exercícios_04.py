"""
# Ex 01: Faça um programa que leia um número inteiro e o imprima.

numero_inteiro = int(input('Informe um número inteiro: '))
print(f'Você informou o número: {numero_inteiro}')

# Ex 02: Faça um programa que leia um número real e o imprima.

numero_real = float(input('Informe um número real: '))
print(f'Você informou o número: {numero_real}')

# Ex 03: Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
numero1 = int(input('Informe o primeiro número inteiro: '))
numero2 = int(input('Informe o segundo número inteiro: '))
numero3 = int(input('Informe o terceiro número inteiro: '))
print(f'A soma entre {numero1}, {numero2} e {numero3} é: {numero1 + numero2 + numero3}')

# Ex 04: Leia um número real e imprima o quadrado desse número.
numero_real = float(input('Informe um número real: '))
print(f'O quadrado de {numero_real} é {numero_real ** 2}')

# Ex 05: Leia um número real e imprima a quinta parte.
numero_real = float(input('Informe um número real: '))
print(f'A quinta parte de {numero_real} é {numero_real / 5}')

# Ex 06: Leia uma temperatura em Celsius e apresente-a convertida para Fahrenheit.
# Fórmula: F = C * (9.0 / 5.0) + 32.0

celsius = float(input('Informe a temperatura em graus Celsius: '))
fahrenheit = celsius * (9.0 / 5.0) + 32.0
print(f'A temperatura de {celsius} graus celsius em fahrenheit é de {fahrenheit} graus fahrenheit.')

"""

# Ex 07: Leia uma temperatura em Fahrenheit e apresente-a convertida em Celsius.
# Fórmula: C = 5.0 * (F - 32.0) / 9.0

fahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0

print(f'A temperatura de {fahrenheit} graus fahrenheit em celsius é de {celsius:.1f} graus celsius.')
