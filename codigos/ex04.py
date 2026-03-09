#4)	Considerando  a  expressão:  AX  +  BX  +  C  =  1  .Faça  um  algoritmo  que  receba  3  valores  inteiros  A,  B,  e  C  e  calcule  o  valor  de  X .   Dados  os  valores  caso  A  e  B  possuam  valor  0  e  C seja diferente de 1 imprimir “solução impossível”. 

# Entrada de dados
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

# Verificação de viabilidade da solução
# A solução é impossível se (A + B) for 0, pois não existe divisão por zero
if (A + B) == 0:
    if C != 1:
        print("Solução impossível")
    else:
        # Se A+B=0 e C=1, qualquer valor de X satisfaz a equação (0 = 0)
        print("Solução indeterminada (Infinitas possibilidades)")
else:
    # Cálculo de X
    X = (1 - C) / (A + B)
    print(f"O valor de X é: {X:.2f}")
