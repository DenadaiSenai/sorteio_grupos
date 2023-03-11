# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 07:38:40 2023

@author: MARCIO DENADAI
"""

import PySimpleGUI as pg
from sorteio_grupos import *

font=('Arial',24)
pg.theme('DarkBlue')

data = [ str(i) for i in range(1,11)]
# cabecalho = [ f"G{i:02d}" for i in range(1,11)]

excluir='6 9'
_res = sorteio_grupos(40, 3, excluir)['grupos']
res = _res.fillna(0).astype(int).values.tolist()
cabecalho = _res.columns.tolist()

layout = [[pg.B("SORTEAR", font=font), pg.B("SAIR",font=font)],
          [pg.T("Digite a qtde de pessoas:",size=(23,1)), pg.I("32", key="qp", size=(20,1))],
          [pg.T("Digite a qtde mínima por grupo:", size=(23,1)), pg.I("4", key="qm", size=(20,1))],
          [pg.T("Lista de números a excluir:",size=(23,1)), pg.I(excluir, key="lx", size=(20,1))],          
          [pg.Table(res,cabecalho,auto_size_columns=False, visible=True, key='tabela', 
                    justification='center', def_col_width=4)]
    ]

win = pg.Window("SORTEADOR DE GRUPOS", layout, font=font)

while True:
    e,v = win.read()
    print(e,v)
    if e in [pg.WINDOW_CLOSED, 'SAIR']:
        break
    if e in ['tema']:
        pg.theme(v['tema'])
    if e in ['SORTEAR']:
        qm = int(v['qm'])
        qp = int(v['qp'])
        lx = v['lx']
        res = sorteio_grupos(qp, qm, lx)['grupos'].fillna(0).astype(int).values.tolist()
        #print(res)
        win['tabela'].update(values=res, visible=True)
    
win.close()