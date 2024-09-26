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

######################################### CONTEÚDO DA SIDEBAR #########################################
st.sidebar.header("Cronologia")
st.sidebar.write("Utilize as opções abaixo para melhor visualização!")
select_years = st.sidebar.multiselect("Selecione o(s) ano(s):", options=[2021, 2022, 2023, 2024], default=[2021, 2022, 2023, 2024])
select_months = st.sidebar.multiselect("Selecione o(s) meses", options=list(dict_months.values()), default=list(dict_months.values()))
selected_months_numbers = [month for month, name in dict_months.items() if name in select_months]


######################################### CONFIGURAÇÕES DAS VARIÁVEIS #########################################
selected_months_numbers = [month for month, name in dict_months.items() if name in select_months]
df_filtered = df_acidentes_transito.get_dataframe_from_data(select_years, selected_months_numbers)
# Substituindo números dos meses por nomes
df_filtered = df_filtered.groupby(['ano', 'mes']).size().reset_index(name='total_acidentes')
df_filtered['mes_nome'] = df_filtered['mes'].map(dict_months)

fig_graph_lines = px.line(df_filtered, x='mes_nome', y='total_acidentes', color='ano', labels={'mes_nome': 'Mês', 'total_acidentes': 'Total de Acidentes'}, title="Evolução Mensal dos Acidentes por Ano")

# Cálculo das métricas
total_acidentes = df_filtered['total_acidentes'].sum()
media_mensal_acidentes = df_filtered['total_acidentes'].mean()

# Cálculo das métricas
total_acidentes = df_filtered['total_acidentes'].sum()
media_mensal_acidentes = df_filtered['total_acidentes'].mean()

# Mês e Ano com maior número de acidentes
row_max_acidentes = df_filtered.loc[df_filtered['total_acidentes'].idxmax()]
mes_max_acidentes = row_max_acidentes['mes']
ano_max_acidentes = row_max_acidentes['ano']
total_max_acidentes = row_max_acidentes['total_acidentes']

# Mês e Ano com menor número de acidentes
row_min_acidentes = df_filtered.loc[df_filtered['total_acidentes'].idxmin()]
mes_min_acidentes = row_min_acidentes['mes']
ano_min_acidentes = row_min_acidentes['ano']
total_min_acidentes = row_min_acidentes['total_acidentes']

# Substituindo números dos meses por nomes
df_filtered['mes_nome'] = df_filtered['mes'].map(dict_months)

######################################### EXIBIÇÃO DAS MÉTRICAS #########################################
st.subheader("Métricas Resumidas")

######################################### GRÁFICO DE BARRAS HORIZONTAIS #########################################
# Criando um DataFrame com as informações dos meses com maior e menor número de acidentes
df_extremos = {
    "Mês": [f"{dict_months[mes_max_acidentes]} ({ano_max_acidentes})", f"{dict_months[mes_min_acidentes]} ({ano_min_acidentes})"],
    "Total de Acidentes": [total_max_acidentes, total_min_acidentes]
}

# Criando gráfico de barras horizontal
fig_bar = px.bar(df_extremos, y="Total de Acidentes", x="Mês", orientation='v', 
                 title="Mês com Maior e Menor Número de Acidentes",
                 labels={"Total de Acidentes": "Total de Acidentes", "Mês": "Mês"})



st.markdown("### Análise Temporal das Ocorrências de Acidentes")
st.write("Nesta seção, você encontrará uma análise clara e objetiva da evolução dos acidentes de trânsito ao longo dos últimos quatro anos. Nosso objetivo é permitir que você visualize, de maneira simples e interativa, como os acidentes se comportaram ao longo do tempo e quais os períodos mais críticos.")
st.markdown("---")

column_metric, column_graph = st.columns([1, 2])

with column_metric:
    st.plotly_chart(fig_bar)

with column_graph:
    st.plotly_chart(fig_graph_lines)
