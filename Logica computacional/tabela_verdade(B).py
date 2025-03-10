# ¬P ^ (¬Q -> R)
P = input('Digite um valor para P: "V" OU "F": ').lower()
Q = input('Digite um valor para Q: "V" OU "F": ').lower()
R = input('Digite um valor para R: "V" OU "F": ').lower()

# Criar variáveis separadas para as negações

if P=="v":
    neg_P = "f"
else:
    neg_P = "v"

if Q=="v":
    neg_Q = "f"
else:
    neg_Q = "v"

# Expressão (¬Q -> R), que equivale a (¬Q == False or R == True)
if neg_Q == "v" and R == "f":
    A = False
else:
    A = True

# Expressão ¬P ^ (¬Q -> R)
if neg_P == "f" and A:
    print('Essa expressão é verdadeira')
else:
    print('Essa expressão é falsa')









    
P = input('Digite um valor para P: "V" OU "F": ').strip().lower() == "v"
Q = input('Digite um valor para Q: "V" OU "F": ').strip().lower() == "v"
R = input('Digite um valor para R: "V" OU "F": ').strip().lower() == "v"

# Negação de P e Q
not_P = not P
not_Q = not Q

# Expressão (¬Q → R), que é equivalente a (¬Q == False or R == True)
implication = not_Q or R

# Expressão final ¬P ∧ (¬Q → R)
result = not_P and implication

# Exibir o resultado
if result:
    print('Essa expressão é verdadeira')
else:
    print('Essa expressão é falsa')
