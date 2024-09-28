import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from database.module_db import df_acidentes_transito

######################################### CONTEÚDO DA SIDEBAR #########################################
st.sidebar.header("Ocorrências")
st.sidebar.write("Observe os vlaores das ocorrências ao decorrer dos anos!")

select_years = st.sidebar.multiselect("Selecione o(s) ano(s):", options=[2021, 2022, 2023, 2024], default=[2021, 2022, 2023, 2024])

######################################### CONTEÚDO DA PÁGINA - MAPA #########################################
st.markdown("### Análise das Ocorrências de Acidentes")
st.markdown('---')
st.markdown('### Overview')
st.html("""
        <p style="text-align: justify !important;"> Esta página fornece uma visão detalhada das ocorrências de acidentes de trânsito no Brasil, incluindo as causas, condições de tráfego e fatores geográficos. Utilizando dados coletados pela Polícia Rodoviária Federal, oferecemos uma análise interativa para compreender melhor os padrões desses acidentes. </p>
""")

st.markdown('---')
st.html("""
        <p style="text-align: justify !important;"> O gráfico a seguir apresenta a distribuição das ocorrências de acidentes de trânsito em diferentes estados. Essa análise detalha quantos acidentes foram registrados em cada unidade da federação, permitindo identificar quais regiões enfrentam maior incidência de acidentes. Essa visualização também possibilita a comparação entre estados, destacando variações regionais que podem estar relacionadas a fatores como densidade populacional, condições das vias e hábitos de condução. </p>
""")
ocorr_uf_ano = df_acidentes_transito.get_dataframe_from_data(select_years).groupby(['uf', 'ano']).size().reset_index(name='Número de Ocorrências')
fig_uf_ano = px.bar(ocorr_uf_ano, x='uf', y='Número de Ocorrências', color='ano',
             title='Ocorrências de Acidentes por Estado (Divididas por Ano)',
             labels={'UF': 'Estado', 'Número de Ocorrências': 'Ocorrências'},
             color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_uf_ano)

st.markdown('---')
st.html("""
        <p style="text-align: justify !important;"> A seguir, apresentamos um gráfico que ilustra a distribuição das ocorrências de acidentes por tipo. Essa visualização permite identificar quais tipos de acidentes são mais frequentes, proporcionando insights valiosos para a análise de segurança no trânsito e a formulação de estratégias de prevenção. </p>
""")
ocorr_tipo = df_acidentes_transito.get_dataframe_from_data(select_years).groupby(['tipo_acidente']).size().reset_index(name='Número de Ocorrências')
fig_tipo = px.bar(ocorr_tipo, x="tipo_acidente", y="Número de Ocorrências", color='tipo_acidente',
            title='Ocorrências de Acidentes por Tipo de Acidente',
            labels={'UF': 'Estado', 'Número de Ocorrências': 'Ocorrências'},
            color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig_tipo)

st.markdown('---')
ocorr_vit = df_acidentes_transito.get_dataframe_from_data(select_years)[['ilesos', 'mortos', 'feridos_leves', 'feridos_graves']].sum()
fig_vit = px.pie(ocorr_vit, 
                 values=ocorr_vit.values, 
                 names=ocorr_vit.index, 
                 title='Distribuição de Vítimas por Categoria')

column_text, column_fig = st.columns([2, 1])

# Texto na primeira coluna

with column_text:
    st.markdown("### Proporção de Vítimas de Ocorrências")
    st.html("""
        <p style="text-align: justify !important;"> A análise das ocorrências de acidentes mostra que, em muitas situações, o número de feridos leves e ilesos é significativamente maior, enquanto as ocorrências de feridos graves e mortes são relativamente baixas. Esse padrão sugere que, apesar de um número elevado de acidentes, muitos deles resultam em consequências menos severas, possivelmente devido a fatores como uso de cintos de segurança, dispositivos de segurança em veículos e a conscientização dos motoristas. </p>
""")

with column_fig:
    st.write(fig_vit)
