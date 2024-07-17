# Um programa que leia o primeiro nome do usuario, se o nome conter 4 letras ou menos escreva "Seu nome é curto" entre 5-6 " Seu nome é normal" mais que 6 "O seu nome é grande"

nome = str(input("Digite o seu nome: "))

tamanho = len(nome)

if tamanho <= 4:
    print("O seu nome é curto")

if tamanho >= 5 and tamanho <= 6:
    print("O seu nome é normal")

if tamanho >= 7:
    print("O seu nome é grande")