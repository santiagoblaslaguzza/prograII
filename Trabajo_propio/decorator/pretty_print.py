# Pretty_Print.py
# Contiene el metodo para que la salida cuando se repiten condimentos sea double triple o nx.

def impresion( description) -> str:
    #print(description)
    lista = description.split(", ")
    print(lista)
    unicos= list(dict.fromkeys(lista[1:]))
    texto = lista[0]
    for i in unicos:
        cant = lista.count(i)
        if cant == 1:
            texto= texto + ", "+ i
        elif cant == 2:
            texto= texto + ", Double "+i
        elif cant == 3:
            texto= texto + ", Triple "+i
        else:
            texto= texto + ", "+ str(cant)+"x "+i
    return texto 
