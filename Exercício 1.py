#Juros compostos 

A1 = float(input("Digite o valor do investimento: "))
A2 = float (input("Digite o número de meses da aplicação: "))
A3 = float (input ("Digite a rentabilidade: "))

FV = A1*( 1+A3 / 100)**A2

print ( f"\nO valor do montante final é de:{ FV:,.2f}\n  \n E o juros composto é: {FV-A1} ") 