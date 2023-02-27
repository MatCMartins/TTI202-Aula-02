def divisao(a,b):
    condicao = False
    while condicao == False:
        if b == 0:
            print("Este denominador é inválido. Insira os valores novamente! ")
        else:
            condicao = True
            return a/b
        