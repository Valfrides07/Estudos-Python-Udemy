# Calculadora

valor_01 = []
valor_02 = []

while True:
    # Tente essa estrutura
    try:
        numero_01 = int(input("Digite o primeiro valor: "))
        valor_01.append(numero_01)

        numero_02 = int(input("Digite o segundo valor: "))
        valor_02.append(numero_02)

        operador = input("Digite o Operador (+, /, -, *) : ")
    
        operadores_permitidos = "+/-*"
        if operador not in operadores_permitidos: # Operadores que nao estajem entre "Operadores_permitidos" irá voltar para iteração
            print("Operadores não permitidos, digite novamente.")
            continue
             
        if operador == "-":
            if numero_01 > numero_02:
                sub1 = numero_01 - numero_02
                print(f"A subtração entre {numero_01} e {numero_02} é: {sub1}")
            else:
                sub2 = numero_02 - numero_01
                print(f"A subtração entre {numero_02} e {numero_01} é: {sub2}")
            break

        elif operador == "+":
            soma01 = numero_01 + numero_02
            print(f"A soma entre {numero_01} e {numero_02} é: {soma01}")
            break

        elif operador == "/":
            if numero_02 or numero_01 == 0:
                print("A divisão é por zero, então não é permitida.")
                continue
            divi = numero_01 / numero_02
            print(f"A divisão entre {numero_01} e {numero_02} é: {divi}")
            break

        elif operador == "*":
            mult = numero_01 * numero_02
            print(f"A Multiplicação entre {numero_01} e {numero_02} é: {mult}")
            break
    # Caso Try de erro, executa except reiniciando o programa
    except ValueError:
        print("Digite um numero válido.")
        continue
