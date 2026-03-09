#8)	Elabore  um  algoritmo  que  construa  uma  matriz  quadrada  de  tamanho  N  em  formato de caracol. Para N igual a 5, a matriz ficará da seguinte forma: 
#Considerações:
#A  matriz  quadrada  é  a  aquela  que  possui  o  número  de  linhas  igual  ao  número  de colunas

# Entrada do tamanho da matriz
N = int(input("Digite o tamanho da matriz quadrada (N): "))

# Inicialização da matriz N x N com zeros
matriz = [[0] * N for _ in range(N)]

num = 1
# O loop percorre as 'camadas' da matriz, de fora para dentro
for i in range((N + 1) // 2):
    
    # 1. Preenche a linha superior (da esquerda para a direita)
    for j in range(i, N - i):
        matriz[i][j] = num
        num += 1
        
    # 2. Preenche a coluna da direita (de cima para baixo)
    for j in range(i + 1, N - i):
        matriz[j][N - i - 1] = num
        num += 1
        
    # 3. Preenche a linha inferior (da direita para a esquerda)
    for j in range(N - i - 2, i - 1, -1):
        matriz[N - i - 1][j] = num
        num += 1
        
    # 4. Preenche a coluna da esquerda (de baixo para cima)
    for j in range(N - i - 2, i, -1):
        matriz[j][i] = num
        num += 1

# Exibição formatada da matriz
print(f"\nMatriz Caracol {N}x{N}:")
for linha in matriz:
    # Formatação com join para remover os colchetes e melhorar a leitura
    print(" ".join(f"{item:02d}" for item in linha))