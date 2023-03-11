#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:49:32 2023

@author: Marcio Denadai
"""

from random import shuffle, seed
import time
import pandas as pd

# Formatar os números nas colunas

pd.options.display.float_format = '{:02.0f}'.format

def sorteio_grupos(qtde_part=34, qtde_min_grupo=4, excluir=[]):
   
    # Cria um lista de numeros aleatoriamente com a qtde de alunos
    amostra = [i for i in range(1,qtde_part+1) if str(i) not in excluir]
    #amostra = []
    #for i in list(range(1,qtde_part+1)):
    #    if i not in excluir:
    #        amostra.append(i)
    _amostra = amostra.copy()

    tam_amostra = len(amostra)
    #print(amostra, tam_amostra)

    total_grupos = int(tam_amostra / qtde_min_grupo)
    resto = int(tam_amostra % qtde_min_grupo)
    
    sorteio = _amostra.copy()
    seed(time.time())
    shuffle(sorteio)
    # for i in range(tam_amostra):
        
        #tam = len(amostra)
        # sorteio.append(amostra.pop(random.randint(0,len(amostra)-1))) 
        # print(amostra,i)
    
    #print(f"{amostra}, {sorteio}, {len(sorteio)}")
        
    # Cria os grupos da lista de sorteio   
    grupos = {'id': range(1,qtde_min_grupo+2)}
    for i in range(total_grupos):
        grupos[f"G{i+1:02d}"] = sorteio[i*qtde_min_grupo : (i+1)*qtde_min_grupo]
        # print(grupos)

    # Aloca os integrantes faltantes nos grupos, para pegar a lista reversamente (ultimos)
    for i in range(1,resto+1):
        grupos[f"G{i:02d}"].append(sorteio[-i])

    df_grupos = pd.DataFrame.from_dict(grupos, orient='index').transpose()
    #df_grupos.set_index('id')
    #df_grupos.style.format('{:02.0f}')
    #df_grupos.set_index('id')
        
    return { "sorteio": sorteio, "total_grupos": total_grupos, "resto": resto, "qtde_part": tam_amostra, 
             "qtde_min_grupo": qtde_min_grupo, "grupos": df_grupos, 'amostra': _amostra
        }

if __name__ == "__main__":
    import sys
    #print(sys.argv)
    if len(sys.argv)>3:
        p1 = int(sys.argv[1])
        p2 = int(sys.argv[2])
        #try:
        p3 = list(sys.argv[3])
        print(p3)
        #except:
        #    p3 = []
        if p1>=p2:
            #print(p1,p2,type(p1),type(p2))
            res = sorteio_grupos(p1,p2,p3)
        else:
            print("""
Uso: python3 sorteio_grupos.py <qtde_de_participantes> <qtde_min_grupo>
            <qtde_de_participantes> tem que ser maior que <qtde_min_grupo>
            
""")
            exit(-1)
    else:
        res = sorteio_grupos(33,4,[2,9,4])
    
#     print(res['grupos'], '\n',res['amostra'], len(res['amostra']))
#     # print(res['grupos'].describe())

