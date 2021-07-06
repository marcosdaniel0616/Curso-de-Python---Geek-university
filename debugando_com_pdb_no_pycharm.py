"""
Debugando com PDB

PDB - Python Debugger

Bug -> Inseto

# OBS: A utilização do print para debuggar código é uma prática ruim.
def dividir(a, b):
    print(f'a = {a}, b = {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))

"""

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o Pycharm ou utilizando
# o PDB - Python Debugger

# Exemplo com o Pycharm


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'


print(dividir(4, 7))
