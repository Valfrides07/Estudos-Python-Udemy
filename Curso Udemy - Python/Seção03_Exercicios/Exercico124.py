# Sistemas de perguntas e respostas
qtd_acertos = 0
qtd_erros = 0

Perguntas = [
    #Pergunta-1
    {
        "Pergunta": "Em qual ano foi descoberto o Brasil?",
        "Opcoes": ["1320", "1502", "1500", "1700"],
        "Resposta_Correta": "3",
    },
    #Pergunta-2
    {
        "Pergunta": "Qual é o nome da pessoa que descobriu o Brasil?",
        "Opcoes": ["Fernão Mendes Pinto", "Pêro da Covilhã", "Vasco da Gama", "Pedro Alvares Cabral"],
        "Resposta_Correta": "4",
    },
    #Pergunta-3
    {
        "Pergunta": "Qual é o nome do último governante do antigo Império Brasil?",
        "Opcoes": ["D. Pedro I", "Isabel I", "D. Pedro II", "D. Afonso I do Brasil"],
        "Resposta_Correta": "3",
    },
    #Pergunta-4
    {
        "Pergunta": "Em que ano o Brasil declarou sua independência de Portugal?",
        "Opcoes": ["1822", "1808", "1831", "1889"],
        "Resposta_Correta": "1",
    },
    #Pergunta-5
    {
        "Pergunta": "Qual era a primeira capital do Brasil colonial?",
        "Opcoes": ["Rio de Janeiro", "São Paulo", "Salvador", "Recife"],
        "Resposta_Correta": "3",
    },
    #Pergunta-6
    {
        "Pergunta": "Quem foi o primeiro imperador do Brasil?",
        "Opcoes": ["D. Pedro I", "D. Pedro II", "D. João VI", "D. Manuel I"],
        "Resposta_Correta": "1",
    },
    #Pergunta-7
    {
        "Pergunta": "Em que ano foi proclamada a República do Brasil?",
        "Opcoes": ["1889", "1822", "1930", "1945"],
        "Resposta_Correta": "1",
    },
    #Pergunta-8
    {
        "Pergunta": "Em que ano foi assinada a Lei Áurea, que aboliu a escravidão no Brasil?",
        "Opcoes": ["1888", "1871", "1827", "1890"],
        "Resposta_Correta": "1",
    },
    #Pergunta-9
    {
        "Pergunta": "Quem foi a princesa responsável pela assinatura da Lei Áurea?",
        "Opcoes": ["Isabel II", "Dona Maria I", "Dona Teresa Cristina", "Dona Leopoldina"],
        "Resposta_Correta": "1",
    },
    #Pergunta-10
    {
        "Pergunta": "Qual foi o papel do Brasil na Segunda Guerra Mundial?",
        "Opcoes": ["Aliado dos Estados Unidos", "Neutro", "Aliado da Alemanha", "Neutro e em paz"],
        "Resposta_Correta": "1",
    }
]

# Numerando cada pergunta 1- 10
for i, pergunta in enumerate (Perguntas):
    print(f"{i+1}º Pergunta:", pergunta["Pergunta"])
    print()
    
    for ni, opcao in enumerate (pergunta["Opcoes"]):
        print(f"{ni+1}º Opção: ", opcao)
    
    opcoes = pergunta["Opcoes"] # Mesmo indíce da lista 'perguntas' atribuido nessa varivel, para evitar conflitos ou erro de sintaxe
    qtd_opcoes = len(opcoes)
    escolhas_int = None
    acertou = False
    
    escolhas_opcoes = input("Digite a opção desejada: ")
    
    if escolhas_opcoes.isdigit():
        escolhas_opcoes_int = int(escolhas_opcoes)
    
    # Verifica se a opção escolhida é válida (dentro do intervalo de opções). Se for, compara com a resposta correta. Se for igual, define acertou como True.
    if escolhas_opcoes_int is not None and 1 <= escolhas_opcoes_int <= qtd_opcoes: # Verifica se escolhas_opcoes_int tem um valor diferente de None.
        if escolhas_opcoes_int == int(pergunta["Resposta_Correta"]):
            acertou = True
                
    if acertou:
        print("Voce acertou!")
        qtd_acertos +=1
                
    else:
        print("voce não acertou.")
        qtd_erros +=1
     
# Se a quantidade de acertos for maior que a de erros, mostra os acertos caso contrário, os erros.
if qtd_acertos >= 6:
    print(f"Voce acertou {qtd_acertos} Perguntas, parábens!")
                
else:
    print(f"Voce errou {qtd_erros} Perguntas, tente novamente.")
    
                
    
        
        
   
        
       