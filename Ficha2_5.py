def ex5():
    num = int(input('Insira um valor entre 1 e 15: '))
    while(num<=15):
        if (num >= 1):
            soma = soma + num
            num = num + 1
        else:
            print("Número inválido")
ex5()