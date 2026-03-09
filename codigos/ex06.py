#Construa um algoritmo que recebe um número inteiro positivo N e gere uma  sequência de números inteiros positivos, de 1 a N. O algoritmo deverá avaliar cada  número dessa sequência da seguinte forma: 
#●	Caso seja um número perfeito, imprimir a mensagem “numero perfeito“; 
#●	Caso seja um múltiplo de 3, imprimir “multiplo de 3”;  ●  Caso seja um múltiplo de 5, imprimir “multiplo de 5”; 
#●	Caso seja um número com a raiz quadrada inteira, imprimir “raiz inteira”. 
#Considerações: 
#Um  número  perfeito  é  um  número  cujo  a  soma  de  todos  os  seus  divisores  naturais próprios (excluindo ele mesmo) é igual ao próprio número. 
#Exemplo:  6  pode  ser  dividido  por  1,  2  e  3,  e  quando  você  soma  esses  números  o  resultado é 6.

import math

# Entrada de dados
n_input = int(input("Digite um número inteiro positivo (N): "))

print(f"\nAnalisando a sequência de 1 até {n_input}:")
print("-" * 40)

for i in range(1, n_input + 1):
    propriedades = []

    # 1. Verificação de Número Perfeito
    soma_divisores = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisores += j
    if i > 1 and soma_divisores == i:
        propriedades.append("número perfeito")

    # 2. Verificação de Múltiplo de 3
    if i % 3 == 0:
        propriedades.append("multiplo de 3")

    # 3. Verificação de Múltiplo de 5
    if i % 5 == 0:
        propriedades.append("multiplo de 5")

    # 4. Verificação de Raiz Quadrada Inteira
    raiz = math.sqrt(i)
    if raiz == int(raiz):
        propriedades.append("raiz inteira")

    # Exibição dos resultados encontrados para o número i
    if propriedades:
        print(f"Número {i}: {', '.join(propriedades)}")