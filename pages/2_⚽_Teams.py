import streamlit as st

st.set_page_config(
    page_title="Fifa",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)


df = st.session_state["data"]

clubes = df['Club'].unique()
club = st.sidebar.selectbox('Escolha um time: ', clubes)

df_teams = df[(df['Club'] == club)].set_index('Name')

st.image(df_teams.iloc[0]['Club Logo'])
st.title(df_teams["Club"][0])

colunas = ['Age','Photo','Flag','Overall','Value(£)','Wage(£)','Joined','Height(cm.)']

def formatar_valor_brasileiro(valor):
    valor = valor*7.36
    valor_formatado = "R$ {:,.2f}".format(valor)
    valor_formatado = valor_formatado.replace(",", "_").replace(".", ",").replace("_", ".")
    return valor_formatado

custo = custo = df_teams['Value(£)'].sum()

st.metric(label="Investimento do Clube somando o valor de mercado de todos os jogadores", value=formatar_valor_brasileiro(custo))
# Formata a coluna "Wage(£)" para o padrão brasileiro
df_teams["Wage(£)"] = df_teams["Wage(£)"].apply(lambda x: formatar_valor_brasileiro(x))
df_teams["Value(£)"] = df_teams["Value(£)"].apply(lambda x: formatar_valor_brasileiro(x))

df_time = df_teams[colunas]
df_time = df_time.rename(columns = {'Age':'Idade','Photo':'Foto','Value(£)':'Valor de Mercado','Wage(£)':'Salário Semanal','Joined':'Início no time','Height(cm.)':'Altura','Flag':'Nacionalidade'})


st.dataframe(df_time,
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                "Foto": st.column_config.ImageColumn(),
                "Nacionalidade": st.column_config.ImageColumn("Nacionalidade"),
             })



