def ex7():
    price = float(input('Introduza o preço do produto: '))
    quantidade = int(input('Introduza o amontoado adquirido: '))
    desconto = 0
    if (quantidade >= 500 and quantidade < 1000):
        desconto = price / 100 * 5
        price = price - desconto
        print("Preço final: ", price)
    elif(quantidade >= 1000):
        desconto = price / 100 * 8
        price = price - desconto
        print("Preço final: ", price)
    else:
        print("Preço final: ", price)
ex7()
