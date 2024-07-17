
hora = int(input("Digite o horario: "))

try:

    if hora >= 00 and hora <= 11:
        print(f"Bom Dia, são {hora}")

    elif hora >= 12 and hora <= 17:
        print(f"Bom Tarde, são {hora}")

    elif hora >= 18 and hora <= 23: 
        print(f"Boa Noite, são {hora}")

    else:
        print(f"Horario informado inválido.")

except:
    print("Horario informado não é do tipo inteiro.")