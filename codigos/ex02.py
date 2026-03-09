# 2)	Faça  um  algoritmo  que  receba  4  valores  inteiros  A,  B,  C  e  D.  Dados  os  valores,  se  B  for  maior  do  que  C  e  se  D  for  maior  do  que  A,  e  a  soma  de  C  com  D  for  maior  que  a  soma  de  A  e  B,  e  ainda,  se  ambos,  C  e  D  forem  positivos  e  A  for  par,  escrever  a  mensagem  "Valores  aceitos", se não escrever "Valores não aceitos". 

# Entrada de dados do usuário
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

# Verifica cada condição separadamente
cond1 = B > C
cond2 = D > A
cond3 = (C + D) > (A + B)
cond4 = C > 0 and D > 0
cond5 = A % 2 == 0

# Avalia todas juntas
if cond1 and cond2 and cond3 and cond4 and cond5:
    print("Valores aceitos")
else:
    print("Valores não aceitos")