"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

    # Criação de dicionário

# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])
# print(paises['ru'])

# OBS: Caso tentemos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError.

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada, será retornado o Valor None e não será gerado KeyError

pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

# Podemos definir um valor padrão, para caso não encontremos o objeto com a chave informada
pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')

# Podemos verificar se determinada chave se encontra no dicionário.

print('br' in paises)

print('ru' in paises)

print('Estados unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, float, boolean), inclusive lista, tupla,
# dicionário, como chaves de dicionários.

# Tuplas, por exemplo, são bastante interessantes de serem utilizadas como chaves de dicionários, pois as mesas são
# imutáveis.

localidades = {
    (35.6895, 39.6917): 'Escritório em Tokyo',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 112.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = { 'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum
receita['abr'] = 350

print(receita)

# Forma 2
novo_dado = {'mai': 500}  # receita.update({'mai' : 500})

receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário

# Forma 1
receita['mai'] = 550

print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário, é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas.

"""

# Remover dados de um dicionário

receita = { 'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Em dicionários, precisamos SEMPRE informar a chave, e caso não encontremos o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado
