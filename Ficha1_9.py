numero = int(input('Insira o numero a verificar: '))
impar = 0
reverse = 0
print("numero inserido: ", numero)
while (numero > 0):
    digito = numero%10
    print("Digito a analisar: ", digito)
    if(digito%2==0):
        print("O número é par")
    else:
        print("O número é impar")
        impar = impar*10+digito
    numero = numero//10
    print("Os números impares são:", impar)
while (impar > 0):
    r=int(impar%10)
    reverse = reverse*10 + r
    impar=int(impar/10)
print("O número inverso é:", reverse)