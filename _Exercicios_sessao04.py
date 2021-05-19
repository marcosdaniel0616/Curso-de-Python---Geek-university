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

# Ex 11: Leia uma velocidade em m/s e apresente-a convertida em km/h.
# Fórmula: K = M * 3.6

metros = float(input('Digite a velocidade em m/s: '))
quilometros = metros * 3.6
print(f'A velocidade de {metros:.2f}m/s convertida para km/h fica: {quilometros:.2f}km/h')

# Ex 12: Leia uma distância em milhas e apresente-a em quilômetros.
# Fórmula: K = 1.61 * M

milhas = float(input('Informe a distância em milhas: '))
quilometros = 1.61 * milhas
print(f'A distância de {milhas:.2f} milhas em quilômetros é de: {quilometros:.2f} quilômetros.')

# Ex 13: Leia uma distância em quilômetros e apresente-a em milhas.
# Fórmula: M = K / 1.61

quilometros = float(input('Informe a distância em quilômetros: '))
milhas = quilometros / 1.61
print(f'A distância de {quilometros} convertida em milhas é de: {milhas} miilhas.'

# Ex 14: Leia um ângulo em graus e apresente-o convertido em radianos.
# Fórmula: R = G * PI / 180. PI = 3.14.

graus = float(input('Informe o valor do ângulo em graus: '))
radiano = graus * 3.14 / 180

print(f'O ângulo de {graus:.2f} graus convertido para radiano é de: {radiano:.2f}')
"""

# Ex 15:
