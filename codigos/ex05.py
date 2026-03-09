#5)	Sabendo  da  existência  da  nova  placa  Mercosul,  e  que  um  sistema  precisa  saber  qual  o  tipo  da  placa  em  questão,  faça  um  algoritmo  que  receba  uma  placa  e  imprima  qual  o  padrão  da  placa  informada  e  a  versão  correspondente  da  mesma  placa  no  outro  padrão. 
#Considerações: 
#A  placa  informada,  deverá  ser  validada,  aceitando  somente  letras  maiúsculas  de  A  a  Z ( sem  acentos),  números  positivos  e  estar  no  formato  AAA9999  ou  AAA9A99.  Caso  a  placa  informada  não  cumpra  esses  critérios,  o  algoritmo  deverá  imprimir  “formato inválido”. 
#Exemplo 1:  
#Para a Placa ABC1234:  Padrão: Brasil; 
#Correspondente : ABC1C34. 
#Exemplo 2:  
#Para a Placa ABC1C34: 
#Padrão: Mercosul; 
#Correspondente : ABC1234. 
#Padrao: Brasil; 0, 1, 2, 3,4,5,6,7,8,9; 
#Padrao: Mercosul; A,B,C,D,E,F,G,H,I,J;


def converter_placa():
    placa = input("Digite a placa do veículo: ").upper()

    # Mapeamento para conversão do 5º caractere
    map_num_para_letra = "ABCDEFGHIJ"
    
    # Validação básica de tamanho
    if len(placa) != 7:
        print("formato inválido")
        return

    # Verificação do prefixo (3 primeiras letras) e sufixo (2 últimos números)
    prefixo_ok = placa[:3].isalpha()
    quarto_char_ok = placa[3].isdigit()
    sufixo_ok = placa[5:7].isdigit()

    if not (prefixo_ok and quarto_char_ok and sufixo_ok):
        print("formato inválido")
        return

    char_conversao = placa[4]

    # Lógica para PADRÃO BRASIL (AAA9999)
    if char_conversao.isdigit():
        indice = int(char_conversao)
        corresp = placa[:4] + map_num_para_letra[indice] + placa[5:]
        print("Padrão: Brasil")
        print(f"Correspondente: {corresp}")

    # Lógica para PADRÃO MERCOSUL (AAA9A99)
    elif char_conversao.isalpha() and char_conversao in map_num_para_letra:
        indice = map_num_para_letra.find(char_conversao)
        corresp = placa[:4] + str(indice) + placa[5:]
        print("Padrão: Mercosul")
        print(f"Correspondente: {corresp}")
    
    else:
        print("formato inválido")

converter_placa()