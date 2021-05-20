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

# Ex 07: Leia uma temperatura em Fahrenheit e apresente-a convertida em Celsius.
# Fórmula: C = 5.0 * (F - 32.0) / 9.0

fahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))
celsius = 5.0 * (fahrenheit - 32.0) / 9.0

print(f'A temperatura de {fahrenheit} graus fahrenheit em celsius é de {celsius:.1f} graus celsius.')

# Ex 08: Leia uma temperatura em Kelvin e apresente-a em Celsius.
# Fórmula: C = K - 273.15

kelvin = float(input('Informe uma temperatura em Kelvin: '))
celsius = kelvin - 273.15
print(f'A temperatura de {kelvin} graus kelvin em celsius é de {celsius:.1f} graus celsius')

# Ex 09: Leia uma temperatura em graus celsius e apresente-o em kelvin.
# Fórmula: K = C + 273.15

celsius = float(input('Informe uma temperatura em Celsius: '))
kelvin = celsius + 273.15

print(f'A temperatura de {celsius} graus celsius em kelvin é de {kelvin} graus kelvin')

# Ex 10: Leia uma velocidade em Km/h (quilômetros por hora) e apresente-o convertido em m/s (metros por segundo)
# Fórmula: M = K / 3.6

quilometros = float(input('Informe uma velocidade em Km/h: '))
metros = quilometros / 3.6
print(f'A velocidade de {quilometros}km/h em metros por segundo é de: {metros:.2f}m/s')

# Ex 11: Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
# Fórmula: K = M * 3.6

metros = float(input('Informe uma velocidade em m/s: '))
quilometros = metros * 3.6
print(f'A velocidade de {metros}m/s em quilômetros por hora é de: {quilometros:.2f}km/h')

# Ex 12: Leia uma distância em milhas e apresente-a convertida em quilômetros.
# Fórmula: K = 1.61 * M

milhas = float(input('Informe uma distância em milhas: '))
quilometros = 1.61 * milhas
print(f'A distância de {milhas} milhas em quilômetros é de {quilometros:.2f} quilômetros.')

# Ex 13: Leia uma distância em quilômetros e apresente-a em milhas.
# Fórmula: M = K / 1.61

quilometros = float(input('Informe uma distância em quilômetros: '))
milhas = quilometros / 1.61
print(f'A distância de {quilometros} quilômetros em milhas é de {milhas:.2f} milhas')

# Ex 14: Leia um ângulo em graus e apresente-o convertido em radianos.
# Fórmula: R = G * 3.14 / 180

graus = float(input('Informe um ângulo em graus: '))
radiano = graus * 3.14 / 180

print(f'O angulo de {graus} graus em radiano é de {radiano} radianos.')

# Ex 15: Leia um ângulo em radiano e apresente-o convertido em graus.
# Fórmula: G = R * 180 / 3.14

radiano = float(input('Informe um ângulo em graus radiano: '))
graus = radiano * 180 / 3.14

print(f'O angulo de {radiano} graus radiano em graus é de {graus:.2f} graus')

# Ex 16: Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
# Fórmula: C = P * 2.54

polegadas = float(input('Informe um comprimento em polegadas: '))
centimetros = polegadas * 2.54
print(f'O comprimento de {polegadas} em centímetros é de: {centimetros:.2f} centímetros')

# Ex 17: Leia um valor de comprimento em centímetros e apresente-o em polegadas.
# Fórmula: P = C / 2.54

centimetros = float(input('Informe um valor em centímetros: '))
polegadas = centimetros / 2.54
print(f'O comprimento de {centimetros} centímetros em polegadas é de {polegadas} polegadas.')

# Ex 18: Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros.
# Fórmula: L = 1000 * M

metros = float(input('Informe um valor de volume em metros cúbicos: '))
litros = 1000 * metros

print(f'O valor de {metros} em metros cúbicos é de {litros:.2f} litros.')

# Ex 19: Leia um valor de volume em litros apresente-o convertido em metros cúbicos m3.
# Fórmula: m = l / 1000

litros = float(input('Informe um volume em litros: '))
metros = litros / 1000

print(f'{litros} litros em metros cúbicos m3 é de {metros:.2f} metros cúbicos')

# Ex 20: Leia um valor de massa em quilogramas e apresente-o convertido em libras.
# Fórmula: L = K / 0.45

quilogramas = float(input('Informe um valor de massa em quilogramas: '))
libras = quilogramas / 0.45

print(f'A massa de {quilogramas} quilogramas em libras é de {libras:.2f} libras')

# Ex 21: Leia um valor de massa em libras e apresente-o convertido em quilogramas.
# Fórmula: K = L * 0.45

libras = float(input('Informe um valor de massa em libras: '))
quilogramas = libras * 0.45
print(f'A massa de {libras} libras em quilogramas é de {quilogramas:.2f} quilogramas')

# Ex 22: Leia um valor de comprimento em jardas e apresente-o convertido em metros.
# Fórmula: M = 0.91 * J

jardas = float(input('Informe o comprimento em jardas: '))
metros = 0.91 * jardas
print(f'{jardas} jardas em metros é de {metros} metros')

# Ex 23: Leia um valor de comprimento em metros e apresente-o convertido em jardas.
# Fórmula: J = M / 0.91

metros = float(input('Informe um valor de comprimento em metros: '))
jardas = metros / 0.91

print(f'{metros} metros em jardas é de {jardas:.2f} jardas')

# Ex 24: Leia um valor de área em metros quadrados m2 e apresente-a convertida em acres.
# Fórmula: A = M * 0.000247

metros = float(input('Informe um valor de área em metros quadrados: '))
acres = metros * 0.000247
print(f'{metros} metros quadrados em acres são {acres} acres.')

# Ex 25: Leia um valor de área em acres e apresente-o convertido em metros quadrados m2.
# Fórmula: m = a * 4048.58

acres = float(input('Informe a área em acres: '))
metros = acres * 4048.58
print(f'A área de {acres} em acres é equivalente a área de {metros} metros quadrados.')

"""


