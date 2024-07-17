# Peça ao usuario que para digitar um numero inteiro e mostre se esse numero é par, mas caso o numero digitado nao seja inteiro, mostre que não é um numero inteiro

try: # Coloca no código que pode gerar um erro dentro do bloco try. Se ocorrer um erro, o Python interrompe a execução normal e pula para o bloco Except
    numero = int(input("Digite o numero: "))
    
    if numero % 2 == 0:
        print("O número digitado é inteiro é par.")
    else:
        print("O numero digitado é inteiro mas não é par")

# except ValueError: é gerado quando uma função recebe um argumento do tipo correto, mas com um valor inadequado,O bloco try-except permite que você trate essa exceção de forma adequada, exibindo mensagens personalizadas ou executando ações específicas quando ela ocorre

except ValueError: 
    print("O numero não é do tipo inteiro")

#try e except, é como se fossem if e o else( caso errado o outro estará certo)