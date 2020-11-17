def ex4():
    num = int(input('Insira um valor entre 1 e 15: '))
    while(num<=15):
        if (num <= 15 and num >= 1):
            print("n =", num)
            num = num + 1
        else:
            print("Número inválido")
ex4()