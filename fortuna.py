def transforma_base(lista):
    dicionario = {}
    if len(lista) == 0:
        return dicionario
    for exr in lista:
        if exr['nivel'] not in dicionario:
            dicionario[exr['nivel']] = []
        dicionario[exr['nivel']].append(exr)
    return dicionario

def valida_questao(questao):
    erros = {}
    # Verifiva se as chaves estão na questão
    chaves = ['titulo','nivel','opcoes','correta']
    for c in chaves:
        if c not in questao:
            erros[c] = 'nao_encontrado'
    
    #Verfica se a questao tem 4 chaves
    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'
    
    #Verifica chave titulo
    if 'titulo' in questao.keys():
        if questao['titulo'].strip() == '':
            erros['titulo'] = 'vazio'

    #Verifica a chave nivel
    if 'nivel' in questao.keys():
        niveis = ['facil','medio','dificil']
        if questao['nivel'] not in niveis:
            erros['nivel'] = 'valor_errado' 

    #Verifica quantidade de opcoes
    if 'opcoes' in questao.keys():
        if len(questao['opcoes']) != 4:
            erros['opcoes'] = 'tamanho_invalido'
        else:
    #Verifica opcoes tenha 4 chaves
            letras = ['A','B','C','D']
            for l in questao['opcoes'].keys():
                if l not in questao['opcoes']:
                    erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                else:
                    if questao['opcoes'][l].strip() == '':
                        if 'opcoes' not in erros:
                            erros['opcoes'] = {}
                        erros['opcoes'][l] = 'vazia'
    
    if 'correta' in questao.keys():
        letras = ['A','B','C','D']
        if questao['correta'] not in letras:
            erros['correta'] = 'valor_errado'
    return erros 