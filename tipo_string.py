"""
Tipo String

Em python, um dado é considerado do tipo string sempre que:

- estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- estiver entre aspas duplas -> "uma string", "234, "a", "True", "42.3"
- estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings,


print(nome[0:4]) # Slice de string
print(nome[5:15]) # Slice de string

print(nome.split()[0])
print(nome.split()[1])
"""
# - estiver entre aspas duplas triplas -> """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,   11,  12,  13, 14]
# ['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']
nome = 'Geek University'

"""
[::-1] -> comece no primeiro elemento, vá até o último e inverta
"""
print(nome[::-1])  # Inversão da string

print(nome.replace('G', 'P'))

print(type(nome))

texto = 'Socorram me subi no onibus em marrocos' # Palíndromo

print(texto)

print(texto[::-1])

nome = 'ana' # Palíndromo

print(nome)

print(nome[::-1])

