def transforma_base(lista):
    dicionario = {}
    if len(lista) == 0:
        return dicionario
    for exr in lista:
        if exr['nivel'] not in dicionario:
            dicionario[exr['nivel']] = []
        dicionario[exr['nivel']].append(exr)
    return dicionario