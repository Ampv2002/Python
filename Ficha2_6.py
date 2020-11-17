def ex6():
    soma = 0
    soma_nums = 0
    num_introduzidos = 0
    media = 0
    while(soma < 500):
        num = int(input('Insira um valor inferior a 100: '))
        if(num < 100):
            soma = soma + num
            soma_nums = soma_nums + num
            num = 0
            num_introduzidos += 1
            print("Soma:", soma)
        else: 
            print("Numero inválido")
    media = soma_nums / num_introduzidos
    print("Média dos valores introduzidos:", media)
ex6()