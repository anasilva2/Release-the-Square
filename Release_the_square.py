# - GRUPO N.: 15
# - ALUNO N.: 79304
# - ALUNO N.: 79496 

# = =  C O N S T A N T E S  = = #

# Dimensoes do tabuleiro

N_LINHAS  = 5
N_COLUNAS = 4

# Tipos de peca

PECA_I = 'I'
PECA_O = 'O'
PECA_U = 'U'
PECA_S = 'S'
ESPACO = 'X'

# Direccoes

NORTE = 'N'
SUL   = 'S'
ESTE  = 'E'
OESTE = 'W'

# = =  T I P O S   A B S T R A C T O S   D E   I N F O R M A C A O  = = #

# ------  TIPO:  COORDENADA  ------ #

linha_coluna_minimo=N_LINHAS-N_COLUNAS

def cria_coordenada(l,c):
    ''' cria_coordenada : int x int -> coordenada
        cria_coordenada(l,c) devolve um elemento do tipo coordenada correspondente
        a posicao (l,c).'''
    
    if not isinstance(l,int) or not isinstance(c,int) or\
       not linha_coluna_minimo <= l <= N_LINHAS or\
       not linha_coluna_minimo <= c <= N_COLUNAS:
        raise ValueError('cria_coordenada: argumentos invalidos')
    else:
        return (l,c)

def coordenada_linha(crd):
    '''coordenada_linha : coordenada -> int
       coordenada_linha(crd) devolve a linha respectiva do elemento coordenada.'''
        
    return crd[0]

def coordenada_coluna(crd):
    ''' coordenada_coluna : coordenada -> int
        coordenada_coluna(crd) devolve a coluna respectiva do elemento coordenada.'''
        
    return crd[1]

def e_coordenada(crd):
    ''' e_coordenada : coordenada -> logico
        e_coordenada(crd) devolve True caso o argumento seja do tipo coordenada 
        e False caso contrario.'''
    
    return isinstance(crd,tuple) and len(crd)==2 and isinstance(coordenada_linha(crd),int) \
       and isinstance(coordenada_coluna(crd),int) and\
       linha_coluna_minimo <= coordenada_linha(crd) <= N_LINHAS and\
       linha_coluna_minimo <= coordenada_coluna(crd) <= N_COLUNAS
        

def coordenadas_iguais(crd1,crd2):
    ''' coordenadas_iguais :  coordenada x coordenada -> logico
        coordenadas_iguais(crd1,crd2) devolve True caso as duas coordenadas sejam
        iguais e False caso contrario.'''
    
    return crd1==crd2
    
def coordenada_na_direcao(crd,dx,dy):
    ''' coordenada_na_direcao : coordenada x int x int -> coordenada
        coordenada_na_direcao(crd,dx,dy) devolve uma coordenada resultante do 
        deslocamento dx linhas e dy colunas a partir da posicao correspondente a
        coordenada crd.'''
    
    if not e_coordenada(crd) or not isinstance(dx,int) or not \
       isinstance(dy,int):
        raise ValueError('coordenada_na_direcao: argumentos invalidos')
    else:
        
        linha_coluna_minimo=N_LINHAS-N_COLUNAS
        
        if crd==(coordenada_linha(crd)+dx,coordenada_coluna(crd)+dy)\
           or (dx==0 and dy==0):
            return False         
        
        if linha_coluna_minimo <= coordenada_linha(crd)+dx <= N_LINHAS and\
           linha_coluna_minimo <= coordenada_coluna(crd)+dy <= N_COLUNAS:
            return cria_coordenada(coordenada_linha(crd)+dx,coordenada_coluna(crd)+dy)
            
        if not linha_coluna_minimo <= coordenada_linha(crd)+dx <= N_LINHAS\
           or not linha_coluna_minimo <= coordenada_coluna(crd)+dy <= N_COLUNAS:
            numero_linhas=coordenada_linha(crd)+dx
            numero_colunas=coordenada_coluna(crd)+dy
            
            if coordenada_linha(crd)+dx > N_LINHAS:
                numero_linhas=N_LINHAS
            if coordenada_linha(crd)+dx < linha_coluna_minimo:
                numero_linhas=linha_coluna_minimo
            if coordenada_coluna(crd)+dy > N_COLUNAS:
                numero_colunas=N_COLUNAS
            if coordenada_coluna(crd)+dy < linha_coluna_minimo:
                numero_colunas=linha_coluna_minimo
                
        if coordenadas_iguais(crd,cria_coordenada(numero_linhas,numero_colunas)):
            return False
        else:
            return cria_coordenada(numero_linhas,numero_colunas)
        
        
# -- Fim: Tipo coordenada -- #


# ---------  TIPO:  PECA  --------- #

pecas={PECA_I:'I',PECA_O:'O',PECA_S:'S',PECA_U:'U', ESPACO:'X'}
peca_estrutura={'I':{'tamanho':2,'est_crd':{0:{'linha':0,'coluna':0},1:{'linha':1,'coluna':0}}},\
                'O':{'tamanho':4,'est_crd':{0:{'linha':0,'coluna':0},\
                                             1:{'linha':1,'coluna':0},\
                                             2:{'linha':0,'coluna':1},\
                                             3:{'linha':1,'coluna':1}}},\
                'S':{'tamanho':1,'est_crd':{0:{'linha':0,'coluna':0}}},\
                'U':{'tamanho':2,'est_crd':{0:{'linha':0,'coluna':0},1:{'linha':0,'coluna':1}}},\
                'X':{'tamanho':1,'est_crd':{0:{'linha':0,'coluna':0}}}} 
direccoes={NORTE:{'dx':-1,'dy':0}, SUL:{'dx':1,'dy':0},ESTE:{'dx':0,'dy':1},OESTE:{'dx':0,'dy':-1}}

def cria_peca(peca,crd):
    ''' cria_peca : cadeia caracteres x coordenada -> peca
        cria_peca(peca,crd) devolve um elemento do tipo peca que corresponde a um
        unico caracter do tipo peca e uma lista de coordenadas correspondentes as
        posicoes da peca.'''
        
    if not peca in pecas or not e_coordenada(crd):
        raise ValueError('cria_peca: argumentos invalidos')
    
    if peca==PECA_S:
        return [peca,[crd]]    
    if peca==PECA_U:
        if (coordenada_coluna(crd)+peca_estrutura[peca]['est_crd'][1]['coluna']) > N_COLUNAS:
            raise ValueError('cria_peca: coordenada invalida')
        return [peca,[crd,(coordenada_linha(crd),coordenada_coluna(crd)+\
                           peca_estrutura[peca]['est_crd'][1]['coluna'])]]
    if peca==PECA_I:
        if (coordenada_linha(crd)+peca_estrutura[peca]['est_crd'][1]['linha']) > N_LINHAS:
            raise ValueError('cria_peca: coordenada invalida')
        return [peca,[crd,(coordenada_linha(crd)+peca_estrutura[peca]['est_crd'][1]['linha'],\
                           coordenada_coluna(crd))]]
    if peca==PECA_O:
        if (coordenada_linha(crd)+peca_estrutura[peca]['est_crd'][3]['linha']) > N_LINHAS\
           or (coordenada_coluna(crd)+peca_estrutura[peca]['est_crd'][3]['coluna']) > N_COLUNAS:
            raise ValueError('cria_peca: coordenada invalida')
        return [peca,[crd,(coordenada_linha(crd)+peca_estrutura[peca]['est_crd'][3]['linha'],\
                           coordenada_coluna(crd)),\
                      (coordenada_linha(crd),\
                       coordenada_coluna(crd)+peca_estrutura[peca]['est_crd'][3]['coluna']),\
                      (coordenada_linha(crd)+peca_estrutura[peca]['est_crd'][3]['linha'],\
                       coordenada_coluna(crd)+peca_estrutura[peca]['est_crd'][3]['coluna'])]]
    if peca==ESPACO:
        return [peca,[crd]]

def peca_posicoes(p):
    ''' peca_posicoes : peca -> lista
        peca_posicoes(p) devolve uma lista contendo todas as coordenadas das
        posicoes ocupadas pela peca p.'''
    
    return p[1]
    
def peca_tipo(p):
    ''' peca_tipo : peca -> cadeia de caracteres
        peca_tipo(p) devolve uma cadeia de caracteres correspondente ao tipo da peca p.'''
    
    return p[0]
    
def e_peca(p):
    ''' e_peca : peca -> logico
        e_peca(p) devolve True se p for um elemento do tipo peca e False caso
        contrario.'''
    
    if p==[] or not isinstance(p,list) or len(p)!=2 or not isinstance(peca_tipo(p),str)\
       or peca_tipo(p) not in pecas or not isinstance(peca_posicoes(p),list) or\
       len(peca_posicoes(p))!=peca_estrutura[peca_tipo(p)]['tamanho']:
        return False
    
    posicoes_peca=peca_posicoes(p)
    tipo_peca=peca_tipo(p)
        
    var=0
    while var < len(posicoes_peca):
        crd_linha=coordenada_linha(posicoes_peca[0])+peca_estrutura[tipo_peca]\
            ['est_crd'][var]['linha']
        crd_coluna=coordenada_coluna(posicoes_peca[0])+peca_estrutura[tipo_peca]\
            ['est_crd'][var]['coluna']
        if not e_coordenada(posicoes_peca[var]) or not\
           coordenadas_iguais(posicoes_peca[var],cria_coordenada(crd_linha,crd_coluna)):
            return False
        var=var+1
        
    return True

def peca_na_posicao(p,c):
    ''' peca_na_posicao : peca x coordenada -> logico
        peca_na_posicao(p,c) devolve True caso a peca p ocupe a posicao
        correspondente a coordenada c, e False caso contrario.'''
    
    pos_peca=peca_posicoes(p)
    i=0
    while i < len(pos_peca):
        if coordenadas_iguais(pos_peca[i],c):
            return True
        i=i+1
    return False

def peca_move(p,dx,dy):
    ''' peca_move : peca x int x int -> {}
        peca_move(p,dx,dy) modifica a posicao da peca p, deslocando-a dx linhas
        e dy colunas.'''
    
    if not e_peca(p) or not isinstance(dx,int) or not isinstance(dy,int):
        raise ValueError('peca_move: argumentos invalidos')
    else:
        pos_peca=peca_posicoes(p)
        nova_pos_peca=[]
        for e in pos_peca:
            nova_pos_peca=nova_pos_peca+[(e[0]+dx,e[1]+dy)]
        for l in range(len(pos_peca)):
            p[1][l]=nova_pos_peca[l]   
        for l in range(len(pos_peca)):
            p[1][l]=nova_pos_peca[l]           
            if not linha_coluna_minimo <= coordenada_linha(p[1][l]) <= N_LINHAS\
               or not linha_coluna_minimo <= coordenada_coluna(p[1][l]) <= N_COLUNAS: 
                nova_pos_peca=[]
                for e in pos_peca:
                    nova_pos_peca=nova_pos_peca+[(e[0]-dx,e[1]-dy)]
                for l in range(len(pos_peca)):
                    p[1][l]=nova_pos_peca[l]
                raise ValueError('peca_move: argumentos invalidos')
        

def posicoes_adjacentes(p,d):
    ''' posicoes_adjacentes : peca x direccao
        posicoes_adjacentes(p,d) devolve uma lista contendo as coordenadas de 
        todas as posicoes do tabuleiro adjacentes a peca p na direcao d.'''
    
    if not e_peca(p) or not d in direccoes:
        raise ValueError('posicoes_adjacentes: argumentos invalidos')
    else:
        nova_lista=[]
        pos_peca=peca_posicoes(p)

        for i in pos_peca:
            if linha_coluna_minimo <= coordenada_linha(i)+direccoes[d]['dx'] <= N_LINHAS and\
               linha_coluna_minimo <= coordenada_coluna(i)+direccoes[d]['dy'] <= N_COLUNAS:
                nova_lista=nova_lista+[cria_coordenada(coordenada_linha(i)+direccoes[d]['dx'],\
                                    coordenada_coluna(i)+direccoes[d]['dy'])]
            else:
                nova_lista=nova_lista+[(coordenada_linha(i)+direccoes[d]['dx'],\
                                                           coordenada_coluna(i)+direccoes[d]['dy'])]                    
                    
        
        for c1 in range(len(pos_peca)-1,-1,-1):
            for c2 in range(len(nova_lista)-1,-1,-1):                    
                if coordenadas_iguais(nova_lista[c2],pos_peca[c1]):
                    del(nova_lista[c2])
        return nova_lista

                                
# -- Fim: Tipo peca -- #


# -------  TIPO: TABULEIRO  ------- #

posicoes_adj_saida=posicoes_adjacentes(cria_peca(PECA_O,cria_coordenada(4,2)),SUL)

def cria_tabuleiro(fich):
    ''' cria_tabuleiro : cadeia de caracteres -> tabuleiro
        cria_tabuleiro(fich) devolve um elemento do tipo tabuleiro que corresponde
        a uma lista de pecas.'''
    
    if not isinstance(fich,str):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    ficheiro=open(fich,'r')
    f=ficheiro.readlines()
    ficheiro.close
               
    lista_pecas=[]
    i=0
    while i < len(f):
        j=0
        while j < len(f[i])-1:
            if f[i][j] in pecas:
                coordenada_peca=cria_coordenada(i+1,j+1)
                if len(lista_pecas)==0:
                    lista_pecas=lista_pecas+[cria_peca(f[i][j],coordenada_peca)]
                else:
                    repeticao=0
                    k=0
                    while k < len(lista_pecas) and repeticao==0:
                        if peca_na_posicao(lista_pecas[k],coordenada_peca):
                            repeticao=1
                        k=k+1
                    if repeticao==0:
                        lista_pecas=lista_pecas+[cria_peca(f[i][j],coordenada_peca)]    
            j=j+1
        i=i+1
    return lista_pecas
    
                
def tabuleiro_posicao(t,c):
    ''' tabuleiro_posicao : tabuleiro x coordenada -> peca
        tabuleiro_posicao(t,c) devolve um elemento do tipo peca que corresponde
        a peca que ocupa a posicao da coordenada c.'''
    
    i=0
    encontra=0
    peca=[]
    while i < len(t) and encontra==0:
        if peca_na_posicao(t[i],c):
            peca=t[i]
            encontra=1
        i=i+1
    if peca_tipo(peca)==ESPACO:
        return ESPACO
    else:
        return peca
    
def actualiza_tabuleiro(t,c,d):
    ''' actualiza_tabuleiro : tabuleiro x coordenada x cadeia de caracteres -> {}
        actualiza_tabuleiro(t,c,d) actualiza/modifica a informacao das pecas no
        tabuleiro t apos mover a peca na posicao correspondente a coordenada c
        uma posicao na direccao d.'''
    
    if not isinstance(t,list) or not e_coordenada(c) or not isinstance(d,str)\
       or d not in direccoes:
        raise ValueError('actualiza_tabuleiro: argumentos invalidos')
     
    for p in t:
        if not e_peca(p):
            raise ValueError('actualiza_tabuleiro: argumentos invalidos')
        

    peca=[]
    indice=0
    cont=0
    while cont < len(t):
        if peca_na_posicao(t[cont],c) and peca_tipo(t[cont])!=ESPACO:
            peca=t[cont]
            indice=cont
        cont=cont+1

    coord_adj=posicoes_adjacentes(peca,d)
    
    i=0
    while i < len(coord_adj):
        j=0
        while j < len(t):
            if peca_na_posicao(t[j],coord_adj[i]) and peca_tipo(t[j])!=ESPACO:
                break
            j=j+1
        i=i+1
    
    peca_move(t[indice],direccoes[d]['dx'],direccoes[d]['dy'])

    nova_lista=[]
    pos_peca=peca_posicoes(t[indice])
    
    for i in pos_peca:
        nova_lista=nova_lista+[cria_coordenada(coordenada_linha(i)-direccoes[d]['dx'],\
                                               coordenada_coluna(i)-direccoes[d]['dy'])]
    
    for c1 in range(len(pos_peca)-1,-1,-1):
        for c2 in range(len(nova_lista)-1,-1,-1):
            if coordenadas_iguais(pos_peca[c1],nova_lista[c2]):
                del(nova_lista[c2])
                
    
    nova_coord_adj=nova_lista 
    h=0    
    for crd in range(len(coord_adj)):
        for k in range(len(t)-1,-1,-1):
            if peca_na_posicao(t[k],coord_adj[crd]) and peca_tipo(t[k])=='X':
                if h < len(nova_coord_adj):
                    t[k]=cria_peca(ESPACO,nova_coord_adj[h])
                h=h+1

                            
def tabuleiro_posicao_livre(t,c):
    ''' tabuleiro_posicao_livre : tabuleiro x coordenada -> logico
        tabuleiro_posicao_livre(t,c) devolve True caso a posicao correspondente
        a coordenada c esteja livre no tabuleiro t, e False caso contrario.'''
    
    if tabuleiro_posicao(t,c)==ESPACO:
        return True
    return False

def e_tabuleiro(t):
    ''' e_tabuleiro : tabuleiro -> logico
        e_tabuleiro(t) devolve True caso t seja do tipo tabuleiro e False caso
        contrario'''
        
    if not isinstance(t,list):
        return False
    
    for peca in t:
        if not e_peca(peca):
            return False
    return True
            
        
# -- Transformador de saida -- #

def desenha_tabuleiro(t):
    ''' desenha_tabuleiro : tabuleiro -> {}
        desenha_tabuleiro(t) desenha o tabuleiro de jogo t para o ecra.'''
    
    DESENHOS = {'TOPO'     : ('+---+','|   |','|   |'),
                'FUNDO'    : ('|   |','|   |','+---+'),
                'ESQUERDA' : ('+----','|    ','+----'),
                'DIREITA'  : ('----+','    |','----+'),
                'TOPOESQ'  : ('+----','|    ','|    '),
                'TOPODIR'  : ('----+','    |','    |'),
                'FUNDOESQ' : ('|    ','|    ','+----'),
                'FUNDODIR' : ('    |','    |','----+'),
                'CENTRO'   : ('+---+','|   |','+---+'),
                'ESPACO'   : ('     ','     ','     ')}    
    
    desenho = [[0] * 4, [0] * 4, [0] * 4, [0] * 4, [0] * 4]

    print('\n      1    2    3    4    ')
    print('   ---------------------- ')
    
    for l in range(N_LINHAS):
        s1 = ''
        s2 = ''
        s3 = ''
        
        for c in range(N_COLUNAS):
            
            if desenho[l][c] == 0:
                p = tabuleiro_posicao(t, cria_coordenada(l + 1, c + 1))
                                
                if p == ESPACO:
                    desenho[l][c] = 'ESPACO'
                elif peca_tipo(p) == PECA_I:
                    desenho[l][c] = 'TOPO'
                    desenho[l+1][c] = 'FUNDO'
                elif peca_tipo(p) == PECA_U:
                    desenho[l][c]     = 'ESQUERDA'
                    desenho[l][c+1]   = 'DIREITA'
                elif peca_tipo(p) == PECA_O:
                    desenho[l][c]     = 'TOPOESQ'
                    desenho[l+1][c]   = 'FUNDOESQ'
                    desenho[l][c+1]   = 'TOPODIR'
                    desenho[l+1][c+1] = 'FUNDODIR'
                elif peca_tipo(p) == PECA_S:
                    desenho[l][c]     = 'CENTRO'
                else:
                    raise ValueError ('desenha_tabuleiro: problema a aceder a tabuleiro')
                    
            s1 = s1 + DESENHOS[desenho[l][c]][0]
            s2 = s2 + DESENHOS[desenho[l][c]][1]
            s3 = s3 + DESENHOS[desenho[l][c]][2]

        print('  |'+ s1+ '| ')
        print(' ' + str(l+1)+ '|'+ s2 +'|'+ str(l+1))
        print('  |'+ s3 +'|')    
    
    print('   ------          ------ ')
    print('      1    2    3    4    ')
        
# - Fim: desenha_tabuleiro
    
# -- Fim: Tipo tabuleiro -- #
 
   
# = =  O U T R A S   F U N C O E S  = = #
    
def jogada_valida(t,c,d):
    ''' jogada_valida : tabuleiro x coordenada x cadeia de caracteres -> logico
        jogada_valida(t,c,d) devolve True se for possivel mover a peca correspondente
        a coordenada c na direccao indicada por d e False caso contrario.'''
    
    if not e_tabuleiro(t) or not e_coordenada(c) or d not in direccoes:
        raise ValueError('jogada_valida: argumentos invalidos')
    else:
    
        if tabuleiro_posicao_livre(t,c):
            return False
        
        peca=tabuleiro_posicao(t,c)
        pos_adj=posicoes_adjacentes(peca,d)
        
        if peca_tipo(peca)==PECA_O and d==SUL and pos_adj==posicoes_adj_saida:
            return True        
        
        for prc in pos_adj:
            if linha_coluna_minimo <= coordenada_linha(prc) <= N_LINHAS and\
               linha_coluna_minimo <= coordenada_coluna(prc) <= N_COLUNAS:
                if not tabuleiro_posicao_livre(t,prc):  
                    return False
            else:
                return False
            
        return True

def pede_jogada():
    ''' pede_jogada : {} -> logico
        pede_jogada() devolve um elemento do tipo coordenada com a linha e coluna
        introduzidas pelo utilizador e uma cadeia de caracteres que corresponde 
        a uma direccao escolhida pelo utilizador.'''
    
    linha=''
    coluna=''
    direccao=''
            
    linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
    while linha=='\n' or not str(1) <= linha <= str(N_LINHAS):
        print('Invalid Line.')
        linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
    
    coluna=str(input('Choose a column (1 to '+str(N_COLUNAS)+'): '))
    while coluna=='\n' or not str(1)<=coluna<=str(N_COLUNAS):
        print('Invalid Column.')
        linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
        while linha=='\n' or not str(1) <= linha <= str(N_LINHAS):
            print('Invalid Line.')
            linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
        coluna=str(input('Choose a column (1 to '+str(N_COLUNAS)+'): '))        

    direccao=raw_input('Choose a direction (N, S, E ou W): ')            
    while direccao=='\n' or not direccao in direccoes:
        print('Invalid Direction.')
        linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
        while linha=='\n' or not str(1) <= linha <= str(N_LINHAS):
            print('Invalid Line.')
            linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))        
        coluna=str(input('Choose a column (1 to '+str(N_COLUNAS)+'): '))
        while coluna=='\n' or not str(1)<=coluna<=str(N_COLUNAS):
            print('Invalid Column.')
            linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))
            while linha=='\n' or not str(1) <= linha <= str(N_LINHAS):
                print('Invalid Line.')
                linha=str(input('Choose a line (1 to '+str(N_LINHAS)+'): '))                        
            coluna=str(input('Choose a column (1 to '+str(N_COLUNAS)+'): '))        
        direccao=raw_input('Choose a direction (N, S, E ou W): ')
        
    return cria_coordenada(int(linha),int(coluna)),direccao

def jogo_terminado(t):
    ''' jogo_terminado : tabuleiro -> logico
        jogo_terminado(t) devolve True caso t corresponda a um jogo terminado, ou
        seja a configuracao da peca 'O' e adjacente a saida, e False caso contrario.'''
    
    if not e_tabuleiro(t):
        raise ValueError('jogo_terminado: argumentos invalidos')
    else:
        indice=0
        for peca in t:
            if peca_tipo(peca)==PECA_O:
                if posicoes_adjacentes(peca,SUL)==posicoes_adj_saida:
                    return True
    return False


def jogo_quadrado(ficheiro_jogo):
    ''' jogo_quadrado : cadeia de caracteres -> {}
        jogo_quadrado(ficheiro_jogo) permite a um utilizador jogar um jogo 
        completo de 'Liberta o quadrado'.'''
    
    if not isinstance(ficheiro_jogo,str):
        raise ValueError('jogo_quadrado: argumentos invalidos')
    else:
        
        tabuleiro_jogo=cria_tabuleiro(ficheiro_jogo)
        desenha_tabuleiro(tabuleiro_jogo)
        
        conta_jogadas=0
        tabuleiro=tabuleiro_jogo
        termina_jogo=False
        
        while termina_jogo==False:
            coordenada,direccao = pede_jogada()
            
            while not jogada_valida(tabuleiro,coordenada,direccao):
                print('Invalid Play.')
                coordenada,direccao = pede_jogada()
                
            if jogada_valida(tabuleiro,coordenada,direccao):
                if jogo_terminado(tabuleiro) and direccao==SUL:
                    conta_jogadas=conta_jogadas+1
                    termina_jogo=True
                    print("Congratulations, you finished the game in ",conta_jogadas,"plays.")
                else:                
                    actualiza_tabuleiro(tabuleiro,coordenada,direccao)
                    conta_jogadas=conta_jogadas+1
                    if jogo_terminado(tabuleiro):
                        termina_jogo=True
                        print("Congratulations, you finished the game in ",conta_jogadas,"plays.")                
                    else:
                        desenha_tabuleiro(tabuleiro)

jogo_quadrado('tab4.txt')
