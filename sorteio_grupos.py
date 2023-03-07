#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 18:49:32 2023

@author: Marcio Denadai
"""

import random
import time
import pandas as pd

def sorteio_grupos(qtde_part=34, qtde_min_grupo=4):
    total_grupos = int(qtde_part / qtde_min_grupo)
    resto = (qtde_part % qtde_min_grupo)
    
    # Cria um lista de numeros aleatoriamente com a qtde de alunos
    amostra = list(range(1,qtde_part+1))
    sorteio = []
    for i in range(qtde_part):
        random.seed(time.time())
        #tam = len(amostra)
        sorteio.append(amostra.pop(random.randint(0,len(amostra)-1))) 
        # print(amostra,i)
        
    # Cria os grupos da lista de sorteio   
    grupos = {'id': range(1,qtde_min_grupo+2)}
    for i in range(total_grupos):
        grupos[f"G_{i+1:02d}"] = sorteio[i*qtde_min_grupo : i*qtde_min_grupo+qtde_min_grupo]

    # Aloca os integrantes faltantes nos grupos
    for i in range(1,resto+1):
        grupos[f"G_{i:02d}"].append(sorteio[-i])

    df_grupos = pd.DataFrame.from_dict(grupos, orient='index').transpose().set_index('id')
        
    return { "sorteio": sorteio, "total_grupos": total_grupos, "resto": resto, "qtde_part": qtde_part, 
             "qtde_min_grupo": qtde_min_grupo, "grupos": df_grupos
        }


if __name__ == "__main__":
    import sys
    #print(sys.argv)
    if len(sys.argv)>2:
        p1 = int(sys.argv[1])
        p2 = int(sys.argv[2])
        if p1>=p2:
            #print(p1,p2,type(p1),type(p2))
            res = sorteio_grupos(p1,p2)
        else:
            print("""
Uso: python3 sorteio_grupos.py <qtde_de_participantes> <qtde_min_grupo>
            <qtde_de_participantes> tem que ser maior que <qtde_min_grupo>
            
""")
            exit(-1)
    else:
        res = sorteio_grupos(39,5)
    
    # print(res['grupos'])
    # print(res['grupos'].describe())

