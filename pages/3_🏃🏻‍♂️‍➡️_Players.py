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

df_players = df[(df['Club'] == club)]

players = df_players['Name'].unique()
player = st.sidebar.selectbox('Jogador ', players)

player_stats = df[(df['Name'] == player)].iloc[0]

st.image(player_stats['Photo'], width=70,)

a,b = st.columns(2)

a.title(f'⭐ {player_stats['Name']}')


b.markdown(f'**Clube** - {player_stats["Club"]}')
b.markdown(f'**Posição** - {player_stats["Position"]}')

st.divider()

st.subheader(f'Overall - {player_stats["Overall"]}')
st.progress(int(player_stats["Overall"]))



a, b, c, d = st.columns(4)

valor_mercado = player_stats["Value(£)"]*7.36
remuneracao = player_stats["Wage(£)"]*7.36
clausula = player_stats["Release Clause(£)"]*7.36

def formatar_valor_brasileiro(valor):
    valor_formatado = "R$ {:,.2f}".format(valor)
    valor_formatado = valor_formatado.replace(",", "_").replace(".", ",").replace("_", ".")
    return valor_formatado


a.metric(label='Valor de mercado', value = formatar_valor_brasileiro(valor_mercado))
b.metric(label='Remuneração semanal', value = formatar_valor_brasileiro(remuneracao))
c.metric(label='Cláusula de rescisão', value = formatar_valor_brasileiro(clausula))





a, b, c, d = st.columns(4)

a.markdown(f'**Nacionalidade** - {player_stats["Nationality"]}')
b.markdown(f'**Idade** - {player_stats["Age"]}')
c.markdown(f'**Altura** - {player_stats["Height(cm.)"] / 100}')
d.markdown(f'**Peso** - {player_stats["Weight(lbs.)"]*0.453:.2f} Kg')


