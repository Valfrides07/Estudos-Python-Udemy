# Uma def que retorne se um numero é par ou impar

def par_impar(numero):
    resul = numero % 2 == 0
    if resul:
        return print (f"{numero} É par")
        
    return print(f"{numero} É impar")

# Retorna True ou falso caso o numero seja par 
print(par_impar(3))
print(par_impar(10))
print(par_impar(34))
print(par_impar(65))
print(par_impar(4))



