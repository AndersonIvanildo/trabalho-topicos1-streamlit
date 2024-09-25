import streamlit as st
import pydeck as pdk
from database.module_db import DF_Acidentes
import plotly.express as px

df_acidentes_transito = DF_Acidentes()

#################################### SIDEBAR ####################################
st.sidebar.header("Selecione Estado e Município")

# INPUTS from USER
uf_selected = st.sidebar.selectbox("Selecione a UF", options=df_acidentes_transito.get_list_uf())

list_city = df_acidentes_transito.get_list_cities(uf_selected)
city_selected = st.sidebar.selectbox("Selecione o Município", options=list_city)

centro_uf = df_acidentes_transito.get_uf_centerpoint(uf_selected)
df_filtrado = df_acidentes_transito.get_dataframe_filtered(uf_selected, city_selected)

# Título principal
st.title('Análise de Acidentes de Trânsito')

# Criação de Tabs
tabs = st.tabs(["Visão Geral", "Mapa de Acidentes", "Distribuição de Acidentes", "Análise de Vítimas", "Análise Temporal"])

# Tab 1 - Visão Geral
with tabs[0]:
    st.header('Estatísticas Gerais')
    st.write(df_acidentes_transito.df_acidentes)
    
# Tab 2 - Mapa de Acidentes
with tabs[1]:
    st.header('Mapa de Acidentes')
    # Configurar o mapa com pydeck
    view_state = pdk.ViewState(
        latitude=centro_uf[0],
        longitude=centro_uf[1],
        zoom=6,
        pitch=0,
    )

    # Criar o mapa com os acidentes do estado selecionado
    st.pydeck_chart(pdk.Deck(
        map_style='light',
        #map_style="mapbox://styles/mapbox/navigation-night-v1",
        initial_view_state=view_state,
        layers=[
            pdk.Layer(
                'HexagonLayer',  # `type` positional argument is here
                df_filtrado,
                get_position='[longitude, latitude]',
                auto_highlight=True,
                elevation_scale=0,
                pickable=True,
                color_range = [
                    [152, 0, 67, 255]
                ],
                elevation_range=[400, 2400],
                extruded=True,
                get_radius=5000,
                coverage=1)
        ],
    ))

    

# Tab 3 - Distribuição de Acidentes por Tipo e Causa
with tabs[2]:
    col1, col2 = st.columns(2)
    st.header('Distribuição de Acidentes por Tipo e Causa')
    fig_1 = px.pie(df_filtrado, names="tipo_acidente", title="Distribuição por Tipo de Acidente")
    fig_2 = px.pie(df_filtrado, names="causa_acidente", title="Distribuição por Causa de Acidente")
    st.plotly_chart(fig_1)
    st.plotly_chart(fig_2)

    
# Tab 4 - Análise de Vítimas
with tabs[3]:
    st.header('Análise de Vítimas')
    fig = px.pie(df_filtrado, names="classificacao_acidente", title="Gráfico de Pizza")
    st.plotly_chart(fig)

# Tab 5 - Análise Temporal
with tabs[4]:
    st.header('Análise Temporal')
    # Agrupar por ano e mês e contar o número de acidentes
    df_mensal = df_acidentes_transito.df_acidentes.groupby(['ano', 'mes']).size().reset_index(name='total_acidentes')

    # Criar o gráfico de linha com plotly
    fig = px.line(df_mensal, x='mes', y='total_acidentes', color='ano',
                labels={'mes': 'Mês', 'total_acidentes': 'Total de Acidentes'},
                title="Evolução Mensal dos Acidentes por Ano")

    # Personalizar a linha de 2024 (dado incompleto)
    fig.update_traces(mode='lines+markers')

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)

# Sidebar - Exportar Dados
st.sidebar.header('Exportar Dados')
if st.sidebar.button('Download CSV'):
    df_filtrado.to_csv('dados_filtrados.csv', index=False)
    st.sidebar.write('Dados exportados com sucesso!')
