import streamlit as st
import plotly.express as px
from database.module_db import df_acidentes_transito

# Dicionário de mapeamento de meses e seu inverso
dict_months = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

st.write("Nesta seção, você encontrará uma análise clara e objetiva da evolução dos acidentes de trânsito ao longo dos últimos quatro anos. Nosso objetivo é permitir que você visualize, de maneira simples e interativa, como os acidentes se comportaram ao longo do tempo e quais os períodos mais críticos.")
######################################### CONTEÚDO DA SIDEBAR #########################################
st.sidebar.header("Cronologia")
st.sidebar.write("Utilize as opções abaixo paramelhor visualização!")
select_years = st.sidebar.multiselect("Selecione o(s) ano(s):", options=[2021, 2022, 2023, 2024], default=[2021, 2022, 2023, 2024])
select_months = st.sidebar.multiselect("Selecione o(s) meses", options=list(dict_months.values()), default=list(dict_months.values()))
selected_months_numbers = [month for month, name in dict_months.items() if name in select_months]


######################################### CONFIGURAÇÕES DAS VARIÁVEIS #########################################
selected_months_numbers = [month for month, name in dict_months.items() if name in select_months]
df_filtered = df_acidentes_transito.get_dataframe_from_data(select_years, selected_months_numbers)
# Substituindo números dos meses por nomes
df_filtered = df_filtered.groupby(['ano', 'mes']).size().reset_index(name='total_acidentes')
df_filtered['mes_nome'] = df_filtered['mes'].map(dict_months)

fig = px.line(df_filtered, x='mes_nome', y='total_acidentes', color='ano', labels={'mes': 'Mês', 'total_acidentes': 'Total de Acidentes'}, title="Evolução Mensal dos Acidentes por Ano")
st.plotly_chart(fig)