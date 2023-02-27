import funcao_soma

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
        print("O resultado da soma é: ", funcao_soma.Soma(x, y))
    else: 
        print("Opção inválida")
        condicao = True