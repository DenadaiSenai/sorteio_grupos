#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 23:00:34 2023

@author: MARCIO DENADAI
"""
from sorteio_grupos import *
import PySimpleGUIQt as pg

# font = ('Arial', 12)
   
data = [[str(i+x) for i in range(1,11)] for x in range(10)]
widths = [6 for i in range(10)]
# print(data)
layout = [[pg.T("Qtde de participantes:"), pg.I("32", key="qp")],
          [pg.T("Qtde minima de participantes:"), pg.I("4", key="qm")],
          [pg.B("SORTEIO"), pg.B("SAIR")],
          [pg.Table(data, data[0], key='tabela', visible=False, col_widths=widths, 
                    auto_size_columns=False, display_row_numbers=False, font=('Arial', 14), 
                    justification='center')]
          ]

win = pg.Window("Sorteio de grupos", layout, finalize=True)
# win.maximize()
# win['tabela'].widget.heading('#0', text='\n\n')

while True:
    e,v = win.read()
    if e in ('SAIR', pg.WINDOW_CLOSED):
        break
    if e in ['SORTEIO']:
        qm = int(v['qm'])
        qp = int(v['qp'])
        res = sorteio_grupos(qp, qm)
        # pg.Popup(res['grupos'].astype(str), title="Grupos")
        # update_table(res['grupos'], win['tabela'])
        r = res['grupos'].fillna(0).astype(int)
        win['tabela'].update(values=r.astype(str).astype(str).values.tolist(), visible=True)
        win.maximize()
win.close()
