"""
# Ex 1: Faça um programa que leia um número inteiro e o imprima.
numero_inteiro = int(input('Digite um número inteiro: '))
print(numero_inteiro)

# Ex 2: Faça um programa que leia um número real e o imprima.
numero_real = float(input('Digite um número real: '))
print(numero_real)

# Ex 3: Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
print(f'A soma dos números deu {primeiro + segundo + terceiro}')

# Ex 4: Leia um número real e imprima o resultado do quadrado desse número.
numero_real = float(input('Digite um número real: '))
print(f'O quadrado de {numero_real} é {numero_real ** 2}')

# Ex 5: Leia um número real e imprima a quinta parte desse número.
numero_real = float(input('Digite um número real: '))
print(f'A quinta parte de {numero_real} é {numero_real / 5}')

# Ex 6: Leia uma temperatura em graus celsius e apresente-a convertida em graus Fahrenheit.
# Fórmula: F = C * ( 9.0 / 5.0) + 32.0

celsius = float(input('Informe a temperatura em graus celsius: '))
fahrenheit = celsius * (9 / 5) + 32
print(f'{celsius} graus celsius convertidos para fahrenheit ficam {fahrenheit} graus fahrenheit')

# Ex 7: Leia uma temperatura em Fahrenheit e converta para Celsius.
# Fórmula: C = 5.0 * (F - 32.0) / 9.0

fahrenheit = float(input('Informe a temperatura em Graus fahrenheit: '))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0
print(f'{fahrenheit} graus fahrenheit convertidos para celsius ficam {celsius:.1f} graus celsius')

# Ex 8: Leia uma temperatura em graus kelvin e converta-a para celsius.
# Fórmula: C = K - 273.15

kelvin = float(input('Informe a temperatura em graus kelvin: '))
celsius = kelvin - 273.15
print(f'{kelvin} graus kelvin convertidos para celsius ficam {celsius:.1f} graus celsius!')

# Ex 9: Leia uma temperatura em graus Celsius e converta-a para Kelvin.
# Fórmula: K = C + 273.15

celsius = float(input('Informe a temperatura em graus celsius: '))
kelvin = celsius + 273.15
print(f'{celsius} graus celsius convertidos para graus kelvin ficam: {kelvin:.1f} graus kelvin')

# Ex 10: Leia uma velocidade em Km/h (quilômetros por hora) e apresente-a em m/s (metros por segundo).
# Fórmula: M = K / 3.6

quilometros = float(input(f'Digite a velocidade em Km/h: '))
metros = quilometros / 3.6
print(f'A velocidade de {quilometros}km/h convertida para m/s fica: {metros:.2f}m/s')

"""

