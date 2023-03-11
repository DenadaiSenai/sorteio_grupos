# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:05:06 2023

@author: MARCIO DENADAI
"""

import streamlit as st
import pandas as pd
from sorteio_grupos import *

# Formatar os números nas colunas
pd.options.display.float_format = '{:02.0f}'.format

st.title("Sorteador de grupos")

with st.form("Digite os dados paro o sorteio:") as form:
    qtde_participantes = st.number_input("Qual a quantidade de participantes?", value=34, min_value=4, step=1, format="%d")
    qtde_min_grupo = st.number_input("Quantas pessoas por grupo?", value=4, min_value=1, step=1,format="%d")
    excluir = st.text_input("Excluir números:", help = "Separar os números por espaço.")
    submit = st.form_submit_button("SORTEAR")
    if submit:
        # Preparar para a lista de exclusão
        _excluir = excluir.replace(',',' ').split(' ')
        #st.write(_excluir)
        res = sorteio_grupos(qtde_participantes, qtde_min_grupo, _excluir) 
        st.write('Formulário enviado')
        st.write(f"A quantidade de participantes é de {res['qtde_part']} pessoas, sendo {qtde_min_grupo} pessoas por grupo.")
        res['grupos'].set_index('id', inplace=True)
        st.write(res['grupos'].T.style.format('{:02.0f}')) # Apresentação da tabela transversal
        #st.write(pd.DataFrame.from_dict(res['amostra']))
        
