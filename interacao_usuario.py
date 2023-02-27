import funcao_soma
import funcao_subtracao
import funcao_multiplicacao
import funcao_divisao


print("Digite abaixo a operação que deseja realizar")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Radiciação")
print("7 - Fatorial")
print("8 - Sair")
condicao = False
while condicao == False:
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))
        print("O resultado da soma é: ", funcao_soma.soma(x, y))
    elif opcao == 2:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))
        print("O resultado da soma é: ", funcao_subtracao.subtracao(x,y))
    elif opcao == 3:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))
        print("O resultado da multiplicação é:", funcao_multiplicacao.multiplicacao(x,y))
    elif opcao == 4:
        x = int(input("Digite o primeiro valor: "))
        y = int(input("Digite o segundo valor: "))
        print("O resultado da operação é: ", funcao_divisao.divisao(x,y))
    else:
        condicao = True

        
