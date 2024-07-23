# Gerador de CPF

import random

for _ in range(100):
    cpf_nove_digitos = " " #Dentro do loop, esta linha inicializa uma string vazia (com um espaço)
    for n in range(9):
        cpf_nove_digitos += str(random.randint(0,9))
    print(cpf_nove_digitos)
        