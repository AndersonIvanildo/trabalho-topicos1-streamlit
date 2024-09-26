import streamlit as st
from database.module_db import df_acidentes_transito
import plotly.express as px

# Configurações gerais do Streamlit
st.set_page_config(layout="wide")

######################################### CONTEÚDO DA SIDEBAR #########################################
st.sidebar.header("Resumo Geral do Projeto")
st.sidebar.write("Explore nosso data app através do menu de páginas acima!")
st.sidebar.markdown('---')
st.sidebar.write('Sobral, CE - 2024')

######################################### CONTEÚDO DA PÁGINA - RESUMO #########################################
st.markdown("## Acidentes de Trânsito no Brasil: Uma Análise Interativa (2021-2024)")
st.markdown('---')
st.markdown('### Contexto do Projeto')
st.html("""
    <p style="text-align: justify !important;"> O trânsito nas grandes cidades e rodovias brasileiras é uma das principais preocupações quando se trata de segurança pública e mobilidade urbana. Todos os anos, milhares de acidentes são registrados, resultando em danos materiais, ferimentos e, infelizmente, perdas de vidas. Com o objetivo de oferecer uma visão clara e acessível sobre a situação dos acidentes de trânsito no Brasil, este data app foi desenvolvido para apresentar esses dados de forma intuitiva e informativa.</p>

    <p style="text-align: justify !important;"> O dataset utilizado abrange os anos de 2021, 2022, 2023 e 2024, sendo que os dados referentes a 2024 estão incompletos, uma vez que o ano ainda não foi finalizado. As informações coletadas para o ano de 2024 estão atualizadas até o mês de outubro. O dataset baseia-se em registros oficiais de ocorrências de acidentes de trânsito, oferecendo uma visão abrangente dos padrões e tendências no Brasil ao longo desses quatro anos.</p>

    <p style="text-align: justify !important;"> Este data app visa facilitar o entendimento desses dados, permitindo que o usuário explore interativamente informações relevantes sobre as ocorrências, com o intuito de promover uma análise mais profunda e embasada sobre os acidentes de trânsito no país.</p>
""")
st.markdown('---')

st.markdown('### O Dataset')
st.html("""
        <p style="text-align: justify !important;"> O dataset utilizado neste <em>data app</em> refere-se aos Boletins de Acidentes de Trânsito disponibilizados pelo portal de Dados Abertos da Polícia Rodoviária Federal (PRF). Esses dados são essenciais para análises preditivas, como a classificação ou regressão de acidentes, e podem ser acessados diretamente no site oficial da PRF: 
        <a href="https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf" target="_blank">Dados Abertos PRF</a>.
        </p>
  
        <p style="text-align: justify !important;"> O conjunto de dados abrange um total de 30 colunas, contendo informações detalhadas sobre cada ocorrência registrada, como a data e o horário do acidente, o estado (UF), o município, a causa e o tipo de acidente, além de dados sobre vítimas e veículos envolvidos. Algumas das principais informações do dataset são: <strong>Data do Acidente</strong>, <strong>Unidade Federativa (estado) onde ocorreu o acidente</strong>, <strong>Causa do Acidente</strong>, <strong>Tipo do Acidente</strong>, <strong>Gravidade do Acidente</strong>, dentre outras.</p>
        
        <p style="text-align: justify !important;"> Essas variáveis fornecem uma visão abrangente sobre as condições dos acidentes, permitindo uma análise aprofundada de diversos fatores que influenciam as ocorrências no Brasil. O dataset é especialmente útil para identificar padrões, tendências e possíveis medidas de prevenção para reduzir os acidentes nas rodovias do país.</p>

        <p>Abaixo está uma amostra do dataset utilizado.</p>
""")
st.write(df_acidentes_transito.df_acidentes.head(10))
st.markdown('---')
