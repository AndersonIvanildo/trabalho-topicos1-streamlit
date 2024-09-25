import streamlit as st
import pydeck as pdk
from database.module_db import df_acidentes_transito

######################################### CONTEÚDO DA SIDEBAR #########################################
st.sidebar.header("Mapa Interativo")
st.sidebar.write("Observe no mapa as ocorrências de acidentes!")

uf_selected = st.sidebar.selectbox("Selecione a UF", options=df_acidentes_transito.get_list_uf())
center_uf = df_acidentes_transito.get_uf_centerpoint(uf_selected)

isMarked = st.sidebar.checkbox("Apenas Estado")

if isMarked:
    if uf_selected == "Todo o Brasil":
        df_filtered = df_acidentes_transito.df_acidentes
    else:
        df_filtered = df_acidentes_transito.get_dataframe_uf(uf_selected)
else:
    list_city = df_acidentes_transito.get_list_cities(uf_selected)
    city_selected = st.sidebar.selectbox("Selecione o Município", options=list_city)
    df_filtered = df_acidentes_transito.get_dataframe_filtered(uf_selected, city_selected)
    center_uf = [df_filtered['longitude'].iloc[0], df_filtered['latitude'].iloc[0]]

######################################### CONTEÚDO DA PÁGINA - MAPA #########################################
st.markdown("### Mapa Interativo de Acidentes de Trânsito no Brasil")
st.markdown('---')
st.markdown('### Ocorrências de Acidentes')
st.write("Este mapa interativo apresenta a distribuição geográfica dos acidentes de trânsito ocorridos no Brasil. Explore diferentes camadas de dados para entender os padrões regionais e temporais dos acidentes.")
column_data, column_map = st.columns([1, 2])

with column_data:
    st.markdown("### Conjunto de Dados")
    st.write(df_filtered)

with column_map:
    if uf_selected != "Todo o Brasil":
        str_title_column_map = "### " + f'Confira abaixo o mapa para {uf_selected}'
        st.markdown(str_title_column_map)

        # Criar a camada de Dispersão para os acidentes
        scatter_layer = pdk.Layer(
            "ScatterplotLayer",
            df_filtered,
            get_position=['longitude', 'latitude'],
            get_radius=500,
            get_color=[152, 0, 67, 255],  # Cor vermelha
            pickable=True
        )

        # Definir o estado de visualização do mapa
        view_state = pdk.ViewState(
            latitude=center_uf[0],
            longitude=center_uf[1],
            zoom=6,
            pitch=0
        )

        # Renderizar o mapa com ambas as camadas
        r = pdk.Deck(layers=[scatter_layer], initial_view_state=view_state)
        st.pydeck_chart(r, use_container_width=True)
    else:
        st.markdown("### Por favor, selecione um estado!")
