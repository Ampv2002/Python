def ex2():
    comeca = 20
    acaba = 0
    intera = -2
    soma = 0
    for i in range(comeca,acaba,intera):
        soma = soma + 1
    print("A soma é: ",soma)
ex2()
def imprimePares():
    lista = [1,2,3,4,5,6,7,8,9,10,11,12]
    comeca = 0
    acaba = len(lista)
    intera = 2
    for i in range(comeca,acaba,intera):
        print(lista[i])
imprimePares()
def criarListaAlunos():
    numeroAlunos = int(input("Insira o número de alunos da turma:"))
    listaAlunos = [0]*numeroAlunos
    i = 0
    for i in range(0, numeroAlunos, 1):
        nome = input("Insira o nome do aluno: ")
        listaAlunos[i] = nome
    print(listaAlunos)
criarListaAlunos()
