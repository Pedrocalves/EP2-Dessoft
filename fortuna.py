import random

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


def valida_questoes(lista_questoes):
    lista_de_erros = []
    for questao in lista_questoes:
        erros = valida_questao(questao)
        lista_de_erros.append(erros)
    return lista_de_erros


def sorteia_questao(questoes_por_nivel,nivel):
    indice_sorteado = random.randint(0, len(questoes_por_nivel[nivel])-1)
    return questoes_por_nivel[nivel][indice_sorteado]
    

def sorteia_questao_inedita(questoes_por_nivel,nivel,questoes_sorteadas):
    questao_inedita = sorteia_questao(questoes_por_nivel,nivel)
    while questao_inedita in questoes_sorteadas:
        questao_inedita = sorteia_questao(questoes_por_nivel,nivel)
    questoes_sorteadas.append(questao_inedita)
    return questao_inedita
    

def questao_para_texto(questao, id):
    return f"----------------------------------------\nQUESTAO {id}\n\n{questao['titulo']}\n\nRESPOSTAS:\nA: {questao['opcoes']['A']}\nB: {questao['opcoes']['B']}\nC: {questao['opcoes']['C']}\nD: {questao['opcoes']['D']}"