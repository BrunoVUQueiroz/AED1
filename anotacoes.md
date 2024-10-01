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