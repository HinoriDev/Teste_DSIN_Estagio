#7)	Escreva um programa que faça a impressão de um  título formatado e centralizado.  O sistema vai receber o título desejado, separado em 2 partes, sendo uma superior e  outra inferior e deve devolver um título formato e centralizado como no exemplo  abaixo:

# Entrada de dados
titulo_sup = input("Digite o título superior: ").strip()
titulo_inf = input("Digite o título inferior: ").strip()

# De acordo com a regra: o total de caracteres deve ser o dobro do título.
# Para manter a simetria entre as duas linhas, baseamos o cálculo no maior título.
tamanho_base = max(len(titulo_sup), len(titulo_inf))
largura_total = tamanho_base * 2

def imprimir_centralizado(texto, largura_alvo):
    # Calcula quantos hifens sobram para as laterais
    espacos_laterais = largura_alvo - len(texto)
    
    # Divide por 2 para cada lado (ajusta se for ímpar para manter simetria)
    lado_esquerdo = espacos_laterais // 2
    lado_direito = largura_alvo - len(texto) - lado_esquerdo
    
    print(f"{'-' * lado_esquerdo} {texto} {'-' * lado_direito}")

# Execução da formatação
print("\nResultado:")
imprimir_centralizado(titulo_sup, largura_total)
imprimir_centralizado(titulo_inf, largura_total)