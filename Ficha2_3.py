def Descobrir_Maior(n1,n2):
    if (n1>n2):
        print(n1, "é maior")
    elif (n1 == n2):
        print("Os números são iguais")
    else:
        print(n2, "é maior")
numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))
Descobrir_Maior(numero1,numero2)