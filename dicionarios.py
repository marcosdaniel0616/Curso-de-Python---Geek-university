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

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
# Forma 1 - Mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

# OBS 1: Em dicionários, precisamos SEMPRE informar a chave, e caso não encontremos o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor desse objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# Se a chave não existir será gerado um keyError
# OBS: Neste caso o valor removido não é retornado.

"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    produto 2:
        - nome;
        - quantidade;
        - preço;
        
        # 1 - Poderíamos utilizar uma lista para isso? Sim

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos  que saber o índice de cada informação no produto.

# 2 - Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 2, 150.00)

carrinho = [produto1, produto2]
print(carrinho)

# Teríamos  que saber o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'Nome': 'Playstation 4', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'Nome': 'God of War 4', 'Quantidade': 1, 'Preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação.


# Métodos de dicionários.

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Limpar o dicionário

d.clear()

print(d)

# Copiando um dicionário para outro

# Forma 1 # deep copy

novo = d.copy()

print(novo)
d['d'] = 4

print(d)
print(novo)

# Forma 2 # Shallow copy
novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)


"""

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois valores: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave, e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')

print(veja)