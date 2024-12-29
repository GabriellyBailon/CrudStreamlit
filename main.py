import uuid
import streamlit as st
import Controllers.ClienteController as ClienteController
import models.ClienteModel as cliente
import pandas as pd
import Pages.Cliente.inserir_cliente as PageInserirCliente
import Pages.Cliente.listar_clientes as PageListarCliente

import Pages.Cliente.deletar_cliente as PageDeletarCliente

def alterar_dados():
    st.title('Alterar cliente cadastrado')

    id = st.text_input(label='Id:')
    id.replace(' ', '')

    if id != '':
        edit_id = uuid.UUID(id)

        costumerList = []

        for item in ClienteController.SelecionarPorId(edit_id):
            costumerList.append([item.id, item.nome, item.idade, item.profissao])

        if costumerList == []:
            st.error('Não foi encontrado cliente cadastrado com esse Id')
        else:
            df = pd.DataFrame(
            costumerList,
            columns=['Id', 'Nome', 'Idade', 'Profissão'])

            st.table(df)
        edit_nome = st.text_input(label='Nome:')

def exibir_menu():
    st.sidebar.title('Menu')
    opcao = st.sidebar.selectbox(options=['Incluir', 'Alterar', 'Excluir', 'Consultar'], label='Opções')

    if opcao == 'Consultar':
        PageListarCliente.consultar_dados()
    elif opcao ==  'Incluir':
        PageInserirCliente.InserirCliente.inserir()
    elif opcao == 'Alterar':
        alterar_dados()
    elif opcao == 'Excluir':
        PageDeletarCliente.excluir_dados()



exibir_menu()