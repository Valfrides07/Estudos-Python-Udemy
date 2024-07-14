# Registro de nome e idade de usuario.


nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))

if nome and idade:

    print(f"O seu nome digitado é: {nome}")    
    print(f"Seu nome invertido: {nome[::-1]}")# Mostra o nome invertido do usuario

#Verifica se há espaços no nome do usuario
    if " " in nome:
        print("Há espaços no nome do usuario")
    else:
        print(f"Não há espaços no nome.")

#Verifica a existencia da letra N no nome digitado
    if "n" in nome:
        print("Existe a letra N no nome.")

    print(f"A primeira letra do seu nome é: {nome[0]}") #Indice 0, representa a primeira letra digitada 
    print(f"A ultima letra do seu nome é: {nome[-1]}")   
else:
    print("Nome ou Idade inválido.")