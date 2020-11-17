quantia = float(input("Insira a quantia: "))
def calculaTroco_v2(quantia):
    listaNotasMoedas = [50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]
    listaContaNM = [0] * len(listaNotasMoedas)
    # posicao = 0
    comeca = 0
    acaba = len(listaNotasMoedas)
    incrementa = 1
    for i in range(0, len(listaNotasMoedas),1):
        while(quantia - listaNotasMoedas[i] >= 0):
            quantia = quantia - listaNotasMoedas[i]
            listaContaNM[i] = listaContaNM[i] + 1
    # for x in listaContaNM:
    #    if (x != 0):
    #        print(x, "número de notas/moedas de: ", listaNotasMoedas[posicao])
    #    posicao = posicao + 1
    for i in range(comeca,acaba ,incrementa):
        if(listaContaNM[i] != 0):
            print("Devolve ", listaContaNM[i], "notas/moedas de ", listaNotasMoedas[i])
    #print("Notas de 50:", listaContaNM[0])
    #print("Notas de 20:", listaContaNM[1])
    #print("Notas de 10:", listaContaNM[2])
    #print("Notas de 5:", listaContaNM[3])
    #print("Moedas de 2 Euros: ", listaContaNM[4])
    #print("Moedas de 1 Euro: ", listaContaNM[5])
    #print("Moedas de 50 Cêntimos:", listaContaNM[6])
    #print("Moedas de 20 Cêntimos:", listaContaNM[7])
    #print("Moedas de 10 Cêntimos:", listaContaNM[8])
    #print("Moedas de 5 Cêntimos:", listaContaNM[9])
    #print("Moedas de 2 Cêntimos:", listaContaNM[10])
    #print("Moedas de 1 Cêntimo:", listaContaNM[11])
    # for i in listaNotasMoedas:
    #   print i
    # while(i<len(listaNotasMoedas)):
    #   print(listaNotasMoedas[i])
    #   i = i + 1
calculaTroco_v2(quantia)