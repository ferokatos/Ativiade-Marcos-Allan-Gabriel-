def Media(numeros):
    t = len(numeros)
    c = 0
    s = 0
    while c < t:
        s = s + numeros[c]
        c = c + 1
    return s/t
def Maior_numero(numeros):
    c = 0
    t = len(numeros)
    while c < t:
        if c == 0:
            maior = numeros[c]
        elif maior < numeros[c]:
            maior = numeros[c]
        c = c + 1
    return maior
def menor(numeros):
    c = 0
    t = len(numeros)
    while c < t:
        if c == 0:
            menor = numeros[c]
        elif menor > numeros[c]:
            menor = numeros[c]
        c = c + 1
    return menor
def par(numeros):
    c = 0
    s = 0
    t = len(numeros)
    while c < t:
        if numeros[c] % 2 == 0:
            s = s + 1
        c = c + 1
    return s

