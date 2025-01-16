import streamlit as st
import webbrowser
import pandas as pd
import numpy as np
from datetime import datetime


st.set_page_config(
    page_title="Fifa",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.sidebar.markdown('Projeto  ')

if "data" not in st.session_state:
    df = pd.read_csv('input/fifa23.csv',index_col=0)
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]
    df = df.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df


st.title("FIFA 23 ⚽")
st.write("O Football Player Dataset de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas, estatísticas de jogo, detalhes do contrato e afiliações ao clube. Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas, pesquisadores e entusiastas do futebol interessados ​​em explorar vários aspectos do mundo do futebol, pois permite estudar atributos do jogador, métricas de desempenho, avaliação de mercado, análise do clube, posicionamento do jogador e desenvolvimento do jogador ao longo do tempo.")

btn = st.sidebar.button("Dados disponibilizados no Kaggle")

if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.sidebar.markdown("""
### Sobre este projeto

Este projeto foi desenvolvido por [ André Rodrigues](https://www.sacadaweb.com.br)  
> **Créditos:** [Asimov](http://www.asimov.com.br)
""")