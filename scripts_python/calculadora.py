sair = False
while sair == False:
    print("Calculadora APP")
    print("1 - Calcular")
    print("2 - Sair")

    opcao = input("Digite qual opcao voce deseja: ")
    int_opcao = int(opcao)
    if int_opcao == 1:
        valorUm = input("Digite o primeiro valor: ")
        float_valorUm = float(valorUm)

        valorDois = input("Digite o segundo valor: ")
        float_valorDois = float(valorDois)

        operacao = input("Digite qual operacao deseja realizar (+, -, *, /, **, //, %, <, >, ==)")
        match operacao:
            case "+":
                print(valorUm, operacao, valorDois, "=", float_valorUm + float_valorDois)
            case "-":
                print(valorUm, operacao, valorDois, "=", float_valorUm - float_valorDois)
            case "*":
                print(valorUm, operacao, valorDois, "=", float_valorUm * float_valorDois)
            case "/":
                print(valorUm, operacao, valorDois, "=", float_valorUm / float_valorDois)
            case "**":
                print(valorUm, operacao, valorDois, "=", float_valorUm ** float_valorDois)
            case "//":
                print(valorUm, operacao, valorDois, "=", float_valorUm // float_valorDois)
            case "%":
                print(valorUm, operacao, valorDois, "=", float_valorUm % float_valorDois)
            case "<":
                print(valorUm, operacao, valorDois, "=", float_valorUm < float_valorDois)
            case ">":
                print(valorUm, operacao, valorDois, "=", float_valorUm > float_valorDois)
            case "==":
                print(valorUm, operacao, valorDois, "=", float_valorUm == float_valorDois)
            case _:
                print("Operacao invalida")
    elif int_opcao == 2:
        sair = True
    else:
        print("Digite uma opcao valida")
