def q1(pessoas ):

    idade = list(pessoas.values())
    nome = list(pessoas.keys())

    indice = []

    resultado = []

    for index , i in enumerate(idade):
        if(i > 18):
            indice.append(index)
            
    for index , i in enumerate(pessoas):
        if(index in indice):
            resultado.append(nome[index])
    resultado.sort()
    return(resultado)


def q2(lista1 , lista2):
    lista = []
    for i in lista1:
        lista.append(i)
    for i in lista2:
        lista.append(i)
    lista.sort()
    return lista

def q3(valores ):
    pares = []
    impares = []
    for i in valores:
        if(i % 2 == 0):
            pares.append(i)
    for i in valores:
        if(i % 2 == 0):
            impares.append(i)
    tamanho_pares = len(pares)

    while(tamanho_pares > 5):
        tamanho_pares -= 1
        pares.pop(0)
        

    return pares , impares

def q4(lista):
    resultado_string = []
    lista.pop(-1)

    maior = max(lista)
    menor = min(lista)
    meio_esquerdo = 0
    meio_direito = 0

    for index,i in enumerate(lista):
        if(i == maior or i == menor):
            lista.pop(index)
        
    if(lista[1] > lista[0]):
        meio_esquerdo = lista[1]
        meio_direito = lista[0]
    else:
        meio_esquerdo = lista[0]
        meio_direito = lista[1]
        

    resultado = [menor ,  meio_esquerdo, maior , meio_direito  ]

    for i in resultado:
        string = float(i)
    
        resultado_string.append(f"{string:.2f}")

    return(resultado_string)



def main():
    pass

if __name__ == "__main__":
    main()


