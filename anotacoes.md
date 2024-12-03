# Qubra de linha
- \r\n -> CRLF
- \n -> LF
```PYTHON
print(12, 34, 1011, sep="" , end="#")
print(56, 78, sep="-", end ="\n")
print(9, 10, sep ="-". end='\n")
```
# Atalho para PRINT
```
print(nome, sobrenome, end="...\n")
>>> ele esta falando para termina com "..." e adicionou uma quebra de linha "\n"

print(nome, sobrenome, sep"#")
>>> Exime o sobrenome com jogo da velha
```

# STR

"""
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte -> COM ISSO O PYTHON JA SABE O TIPO DE INFORMAÇÃO QUE VOCÊ TA QUERENDO PASSAR PARA ELE.

- str -> string -> texto
"""
# Aspas simples
```python
print('Bruno')
```
# Aspas duplas
```python
print("Bruno")
```
# Escape
```python
print("Bruno \"Queiroz\"")
```
# r
```python
print(r"Bruno \"Queiroz\"")
```
# Variações
caso eu queiro que apareça as aspas
```python
print('Bruno "Queiroz"')
```
# Tipos int e float
 - int -> Número inteiro
 O tipo int representa qualquer número
 positivo ou negativo. int sem sinal é considerado
 positivo.
 ```python
 print(11) # int
 print(-11) # int
 print(0)
 ```

 - float -> Número com ponto flutuante
 O tipo float representa qualquer número
 positivo ou negativo com ponto flutuante.
 float sem sinal é considerado positivo.
 ```python
 print(1.1, 10.11)
 print(0.0, -1.5)
 ```

 - A função type mostra o tipo que o Python
 inferiu ao valor.
 ```python
print(type('Otávio'))
print(type(0))
print(type(1.1), type(-1.1), type(0.0))
```
# Tipo de dado bool (boolean)
 Ao questionar algo em um programa,
 só existem duas respostas possíveis:
- sim (True) ou não (False).
 
 Existem vários operadores para "questionar".
 Dentre eles o ==, que é um operador lógico que
questiona se um valor é igual a outro
```python
print(10 == 10)  # Sim => True (Verdadeiro)
print(10 == 11)  # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 11))
```

# conversão de tipos, coerção
 type convertion, typecasting, coercion
 é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
 str, int, float, bool
 ```python
print(int('1'), type(int('1')))
print(type(float('1') + 1)) #converter em float
print(bool(' '))
print(str(11) + 'b')
```
# Variáveis são usadas para salvar algo na memória do computador.
 PEP8: inicie variáveis com letras minúsculas, pode usar
 números e underline _.

O sinal de = é o operador de atribuição. Ele é usado para
 atribuir um valor a um nome (variável).

 Uso: nome_variavel = expressão
```python
 nome_completo = 'Luiz Otávio Miranda'
 soma_dois_mais_dois = 2 + 2
 int_um = bool('1') #bool_um
 print(int_um, type(int_um))
 print(nome_completo, soma_dois_mais_dois)

nome = 'Luiz'
idade = 17
maior_de_idade = idade >= 18
print('Nome:', nome, 'Idade:', idade)
print('É maior?', maior_de_idade)
```
# Operadores Aritiméticos
````python
adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 10
print('Multiplicação', multiplicacao)

divisao = 10 / 3  # float
print('Divisão', divisao)

divisao_inteira = 10 // 3
print('Divisão inteira', divisao_inteira)

exponenciacao = 2 ** 10
print('Exponenciação', exponenciacao)

modulo = 55 % 2  # resto da divisão
print('Módulo', modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(10 % 2 == 0)
print(15 % 2 == 0)
print(16 % 2 == 0)

    ->Precedência
Sequência de operação
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

````
# Concatenacao 
````python
concatenacao= 'Luiz' + ' ' + 'Otávio'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_luiz = 3 * 'Luiz'
print(a_dez_vezes)
print(tres_vezes_luiz)
````

# Formatação de de String
````python
nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987

a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
) #parâmetro nomeado

print(formato)
````

# Input
````python
# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
# O int foi adicionado aqui ao ives de colocar no input
print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
# nesse codigo ele colocou a coerção de tipo em outra variáveis, para permitir uma chacagem
````
# If / Elif / Else
````python

# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar': #True or False
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')





condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita.')

if 10 == 10:
    print('Outro if')

print('Fora do if')
````

# Operadores Relacionais
````python

"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print('Olha meu print aqui')
````
# Operadores Lógicos
- AND
````python
# Operadores lógicos
# and (e) or (ou) not (não)

#-> and - Todas as condições precisam ser

# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
 senha_digitada = input('Senha: ')

 senha_permitida = '123456'

 if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrar')
 else:
     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
````
- OR
````python
# Operadores lógicos
# and (e) or (ou) not (não)

#-> or - Qualquer condição verdadeira avalia

# toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
 senha_digitada = input('Senha: ')

 senha_permitida = '123456'

 if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
     print('Entrar')
 else:
     print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
````
- NOT
````python
# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
 senha = input('Senha: ')
print(not True)  # False
print(not False)  # True
````
# Operadores IN e NOT IN
````python
# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('vio' in nome)
# print('zero' in nome)
# print(10 * '-')
# print('vio' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')
 
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

````
# Interploção básica de strings
````python
"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
````
# Formatação básica de strings
````python
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
````
# Fatiamento de strings
````python
"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
i = inicio
f = final
p = passo
Obs.: a função len retorna a qtd 
de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[::-1])
print(len(variavel))
print(f"Seu nome tem {len(nome)} letras")
````
# Try/except
````python
"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')
````

# Variaveis, constante e complexidade de código
````python

"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega
vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1
if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
if carro_passou_radar_1:
    print('Carro passou radar 1')
if carro_multado_radar_1:
    print('carro multado em radar 1')
    """
````

# Flags, is, is not e None
````python
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
````

# Informações
Imutáveis que vimos: str, int, float, bool

https://docs.python.org/pt-br/3/library/stdtypes.html

# While + Break
````python
"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
````
````python

contador = 0

while contador <10:
    contador = contador + 1
    print(contador)
print("Acabou")


#outra opção

contador = o

while contador <=10:
    print(contador)
    contador = contador + 1
print("Acabou)
````
# Operadores de atribuição
````python
"""
Operadores de atribuição
=  +=  -=  *=  /=  //=  **=  %=
"""
contador = 10
###
contador /= 5
print(contador)
````
# While + Continue
```python

contador = 0
while contador <= 100:
    contador += 1
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    print(contador)
    if contador == 40:
        break
print('Acabou')
```
# While + While
```python

qtd_linhas = 5
qtd_colunas = 5
linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1
print('Acabou')
```

# While/else
````python
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')
````
# For + Range
```python
"""
podemos ler o "for" dessa maneira: para cada _NOME_ no meu _LISTA_ faça alguma coisa:

for nome in lista:

range -> range(start, stop, setep)
"""
numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)

```
# Tipo list
````python
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
````
# append (list)
````python

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop() #remove o ultimo adicionado
lista.append(60) #adiciona no final da lista
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)
````
# insert (list)
````python

"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(100, 5)
print(lista[4])
````

# extend (list)
````python
"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)
````

# Desempacotamento

````python
"""
Introdução ao empacotamento e desempacotamento
"""
_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)
# "_" serve para pular o índice da lista e você criar outra variável
````
# Tupla - imutável
````python
"""
Tipo tupla - Uma lista imutável
"""
nomes = ('Maria', 'Helena', 'Luiz')
# nomes = tuple(nomes)
# nomes = list(nomes)
print(nomes[-1])
print(nomes)
````
# enumerate
````python
"""
enumerate - enumera iteráveis (índices)
"""
# [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)


# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')
````
# Impressao de ponto fluante
````python
"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal
numero_1 = decimal.Decimal('0.1')# nesse caso é preciso passar o número como string, quando importamos o "decimal"
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
print(round(numero_3, 2))
````
# aplit e join com list e str
````python
"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip tira os espaços do começo e final
"""
frase = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)
````
# Lista dentro de lista
````python
"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)
````
# Interpretador Python

Interpretador do Python

- python mod.py (executa o mod)

- python -u (unbuffered)

- python -m mod (lib mod como script)

- python -c 'cmd' (comando)

- python -i mod.py (interativo com mod)


The Zen of Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Plano é melhor que aglomerado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Embora a praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Deve haver um -- e só um -- modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio à primeira vista a menos que você seja holandês.
Agora é melhor que nunca.
Embora nunca frequentemente seja melhor que *exatamente* agora.
Se a implementação é difícil de explicar, é uma má ideia.
Se a implementação é fácil de explicar, pode ser uma boa ideia.
Namespaces são uma grande ideia -- vamos fazer mais dessas!
"""

# Desempacotamento em chamdas
````python
# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, ap, u = lista
# print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)

print(*salas, sep='\n')
````
# Operação ternária
````python
"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
# condicao = 10 == 11
# variavel = 'Valor' if condicao else 'Outro valor'
# print(variavel)
# digito = 9  # > 9 = 0
# novo_digito = digito if digito <= 9 else 0
# novo_digito = 0 if digito > 9 else digito
# print(novo_digito)
print('Valor' if False else 'Outro valor' if False else 'Fim')
````

