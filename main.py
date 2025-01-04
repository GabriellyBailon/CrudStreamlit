import streamlit as st
import Pages.Cliente.inserir_cliente as PageInserirCliente
import Pages.Cliente.listar_clientes as PageListarCliente
import Pages.Cliente.atualizar_cliente as PageAlterarCliente
import Pages.Cliente.deletar_cliente as PageDeletarCliente

def exibir_menu():
    st.sidebar.title('Menu')
    opcao = st.sidebar.selectbox(options=['Incluir', 'Alterar', 'Excluir', 'Consultar'], label='Opções')

    if opcao == 'Consultar':
        PageListarCliente.consultar_dados()
    elif opcao ==  'Incluir':
        PageInserirCliente.InserirCliente.inserir()
    elif opcao == 'Alterar':
        PageAlterarCliente.alterar_dados()
    elif opcao == 'Excluir':
        PageDeletarCliente.excluir_dados()



exibir_menu()