# Função que calcula o salário líquido
def calcular_salario_liquido(horas_por_dia, dias_trabalhados, preco_hora):
    salario_bruto = horas_por_dia * dias_trabalhados * preco_hora
    desconto = salario_bruto * 0.03  # 3% de desconto
    salario_liquido = salario_bruto - desconto
    return salario_liquido

# Entrada de dados do usuário
horas = int(input("Digite o número de horas trabalhadas por dia: "))
dias = int(input("Digite o número de dias trabalhados no mês: "))
preco = float(input("Digite o preço da hora trabalhada: "))

# Calcula salário líquido
salario = calcular_salario_liquido(horas, dias, preco)

# Mostra o resultado
print(f"O salário líquido do trabalhador é: R$ {salario:.2f}")