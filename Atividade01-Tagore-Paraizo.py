def soma_kleene(a,b):
    def sucessor(x):
        return x+1
    resultado = a 
    contador = 0 
    while contador < b :
        resultado = sucessor(resultado)
        contador = sucessor(contador)
    return resultado 

def potencia_kleene(a,b):
    contador2 = 0
    resultado = 1
    while contador2 < b:
        contador1 =0 
        resultado_temp =0
        while contador1 < a:
            resultado_temp = soma_kleene(resultado_temp,resultado)
            contador1+=1
        contador2+=1
        resultado = resultado_temp
    return resultado 
if __name__ == '__main__':
    print("Testando pontenciação com soma kleene")
    print("resultado",potencia_kleene(2,3))
