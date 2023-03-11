# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 07:38:40 2023

@author: MARCIO DENADAI
"""

import PySimpleGUI as pg
from sorteio_grupos import *

# Configurações iniciais
data = [ str(i) for i in range(1,11)]
# cabecalho = [ f"G{i:02d}" for i in range(1,11)]

excluir='6 9'
_res = sorteio_grupos(40, 3, excluir)['grupos']
res = _res.fillna(0).astype(int).values.tolist()
cabecalho = _res.columns.tolist()

# Iniciar varáveis da janela para o looping principal
tema = 'Reddit' # Tema inicial
fonte = ('Arial',12)
notExit = True  # Variável para travar no looping da troca de tema
while(notExit):
    font = fonte
    pg.theme(tema)

    # Configuração do layout da janela
    layout = [[pg.B("SORTEAR", font=font), pg.B("SAIR",font=font), pg.T("Mudar tema"), pg.Combo(pg.theme_list(), pg.theme(), key="TEMA", enable_events=True)],
            [pg.T("Digite a qtde de pessoas:",size=(23,1)), pg.I("32", key="qp", size=(20,1))],
            [pg.T("Digite a qtde mínima por grupo:", size=(23,1)), pg.I("4", key="qm", size=(20,1))],
            [pg.T("Lista de números a excluir:",size=(23,1)), pg.I(excluir, key="lx", size=(20,1))],          
            [pg.Table(res,cabecalho,auto_size_columns=False, visible=True, key='tabela', 
                        justification='center', def_col_width=4)]
        ]
    # Variável da janela principal
    win = pg.Window("SORTEADOR DE GRUPOS", layout, font=font)

    while True: # Looping principal da janela
        e,v = win.read()
        print(e,v)
        if e in [pg.WINDOW_CLOSED, 'SAIR']:
            notExit = False
            break
        if e in ['SORTEAR']:
            qm = int(v['qm'])
            qp = int(v['qp'])
            lx = v['lx']
            res = sorteio_grupos(qp, qm, lx)['grupos'].fillna(0).astype(int).values.tolist()
            #print(res)
            win['tabela'].update(values=res, visible=True)
        if e in ['TEMA']:
            tema = v['TEMA']
            break
    win.close()

    # Popup para confirmar a saída do programa
    if not notExit:
        x = pg.popup_yes_no(f"Você quer realmente sair?")
        print(x)
        if x=='No':
            notExit = True       
