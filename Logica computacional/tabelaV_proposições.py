# Imprime o cabeçalho da tabela
print(f' P | Q | R | ¬(P v R) | NotPR | NotP | NotQ | (NotP ^ NotQ) | NotPR <-> NotPQ')

# Contadores para classificar a expressão
verdadeiros = 0
falsos = 0

# Laços para gerar todas as combinações de P, Q e R (0 = verdadeiro, 1 = falso)
for a in range(2):  # P pode ser 0 (V) ou 1 (F)
    for b in range(2):  # Q pode ser 0 (V) ou 1 (F)
        for c in range(2):  # R pode ser 0 (V) ou 1 (F)
            
            # Definição de P, Q e R
            P = 'V' if a == 0 else 'F'
            NotP = 'F' if a == 0 else 'V'  # Negação de P
            
            Q = 'V' if b == 0 else 'F'
            NotQ = 'F' if b == 0 else 'V'  # Negação de Q
            
            R = 'V' if c == 0 else 'F'

            # ¬(P v R) → Primeiro fazemos (P v R), depois negamos
            PR = 'V' if P == 'V' or R == 'V' else 'F'  # (P v R)
            NotPR = 'F' if PR == 'V' else 'V'  # Negação de (P v R)

            # (¬P ^ ¬Q) → "NotP e NotQ"
            NotPQ = 'V' if NotP == 'V' and NotQ == 'V' else 'F'

            # Verifica se NotPR e NotPQ são iguais
            Equivalente = 'V' if NotPR == NotPQ else 'F'

            # Contabiliza os valores
            if Equivalente == 'V':
                verdadeiros += 1
            else:
                falsos += 1

            # Exibe a linha da tabela
            print(f'{P} | {Q} | {R} | {NotPR}  | {PR}  | {NotP}  | {NotQ}  | {NotPQ}  | {Equivalente}')

# Classificação da expressão lógica
if falsos == 0:
    classificacao = "Tautologia (sempre verdadeira)"
elif verdadeiros == 0:
    classificacao = "Contradição (sempre falsa)"
else:
    classificacao = "Contingência (verdadeira para alguns casos e falsa para outros)"

# Exibe a classificação
print("\nClassificação da expressão:", classificacao)
