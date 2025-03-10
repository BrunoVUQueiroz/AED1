# P V ¬Q
P = input('Digite um valor para P: "V" OU "F": ').lower()
Q = input('Digite um valor para Q: "V" OU "F": ').lower()
# Negação de Q
if Q == 'v':
    Q = 'f'
else:
    Q = 'v'
# Expressão P ∨ ¬Q
if P =='v' or Q =='v':
    print('Essa condição é verdadeira')
else:
    print('Essa condição é falsa')



