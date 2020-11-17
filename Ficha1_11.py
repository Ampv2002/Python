num = int(input("Digite um número inteiro: "))
zero = 0
zeros_seguidos = 0
seguidos = False
while(num>0):
    digito = num %10
    if (digito==0 and seguidos == True):
        zeros_seguidos = zeros_seguidos + 1
    elif (digito == 0 and seguidos == False):
        zero = zero + 1
        seguidos = True
    else:
        seguidos = False
    num = num//10
    print ("Número de zeros seguidos encontrados: ", zeros_seguidos)