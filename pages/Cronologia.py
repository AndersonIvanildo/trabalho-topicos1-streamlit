import streamlit as st

def render_Overview():
    ##################### Configurações da Sidebar #####################
    with st.sidebar:
        st.header("Menu de Overview")
        st.sidebar.markdown("---")  # Linha de separação
        st.sidebar.markdown("### Equipe 1")  # Nome da equipe

    st.title("Overview - Acidentes de Trânsito")
    st.html("<h4>Trabalho de Tópicos de Computação 1</h4>")
    st.write("Bem-vindo à Página 1!")
    # Sidebar específica para a Página 1
    opcao = st.sidebar.radio("Escolha uma cor para a Página 1:", ["Vermelho", "Azul", "Verde"])
    st.write(f"A cor escolhida para a Página 1 foi: {opcao}")
