#3)	Faça  um  algoritmo  que  receba  um  valor  inteiro.  Dado  o  valor,  calcule  o  menor  número  de  notas ( cédulas)  possíveis  no  qual  o  valor  pode  ser  decomposto.  As  notas  consideradas  são  de 200 , 100 , 50 , 20 , 10 , 5 ,  2  e  1.  A  seguir  mostre  o  valor  lido  e  a  relação  de  notas  necessárias. Exemplo: 
#Para 777: 
#●	3  nota(s) de R$ 200,00 
#●	1  nota(s) de R$ 100,00 
#●	1  nota(s) de R$ 50,00  ● 	1  nota(s) de R$ 20,00 
#●	0  nota(s) de R$ 10,00 
#●	1  nota(s) de R$ 5,00 ●  	1  nota(s) de R$ 2,00 
#●	0  nota(s) de R$ 1,00 

valor = int(input("Digite um valor inteiro: "))
notas = [200, 100, 50, 20, 10, 5, 2, 1]
print(f"Valor: R$ {valor}")
for nota in notas:
    quantidade = valor // nota
    print(f"{quantidade} nota(s) de R$ {nota},00")
    valor -= quantidade * nota

