# Arrumar a lógica, após o usuario enserir uma string o programa não retorna ao inicio como desejado, mas prossegue para a proxima iteração 

import time

def gerador (pergunta):
    for i in range(int(pergunta)):
        print(f"Indo de zero até: {i}")
        time.sleep(0.4) 

while True:
    pergunta = input("Ensira um número que desejar: ")
    
    if pergunta.isdigit(): # É obtido como uma string e é verificado se é composto apenas por dígitos usando o método,se for composto apenas por dígitos, ele é convertido para um inteiro
        pergunta = int(pergunta)
            
    else:
        print("Por favor digite um número que seja válido.")
        gerador(pergunta)
            
    confirmacao = str(input("A pergunta está correta? ")).lower()
    
    if confirmacao == "sim" or confirmacao == "s":
        gerador(pergunta)
        break
    
    elif confirmacao == "nao" or confirmacao == "n":
        print("Por favor digite novamente os numeros desejados")
        continue
            
    else:
        print("Valor digitado inválido, por favor digite um valor que seja válido")
        continue
    