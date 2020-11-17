nota1 = float(input("Escreva a primeira nota:"))
nota2 = float(input("Escreva a segunda nota:"))
media = (nota1+nota2/2)
if(media>=9.5):
    print("O aluno foi aprovado. Média:  ", media)
else:
    print("O aluno não foi aprovado. Média: ", media)