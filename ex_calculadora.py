print ("-="*20)

while True:

    operador = int(input("\nSelecione a operação que deseja realizar \n1- Adicão \n2- Subtração \n3- Multiplicação \n4- Divisão \nSeleção: "))
    numero1 = input("\nDigite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")

    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try: 
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou ambos números são invalidos")
        continue


    if operador == 1:
            soma = num1_float + num2_float

            print("\nA soma dos dois números é: {}".format(soma))
            print("\n")
            print("-="*20 )

    
    elif operador == 2:

            sub = num1_float - num2_float

            print("\nA subtração dos dois números é: {}".format(sub))
            print("\n")
            print("-="*20 )

    elif operador == 3:

            mult = num1_float * num2_float

            print("\nA multiplicação dos dois números é: {}".format(mult))
            print("\n")
            print("-="*20 )

    elif operador == 4:

            div = num1_float / num2_float

            print("\nA divisão dos dois números é: {}".format(div))
            print("\n")
            print("-="*20 )

    else:
        print("\nOperador invalido!")
        continue

    sair = input("\nDeseja sair? Sim/Não: ")
    
    if sair == 'sim' or sair == 'Sim' or sair == "SIM" or sair == "s":
        break

