def somar_valores(valores):
    return sum(valores)

def antecessor_sucessor(valor):
    antecessor = valor - 1
    sucessor = valor + 1
    
    return antecessor, sucessor



print(somar_valores([10, 20, 30, 50]))

print(antecessor_sucessor(70)) # retorna em uma tupla