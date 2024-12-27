import uuid
import streamlit as st
import Controllers.ClienteController as ClienteController
import models.ClienteModel as cliente
import pandas as pd

def alterar_dados():
    st.title('Alterar cliente cadastrado')
    edit_id = st.text_input(label='Id:')

    
    edit_nome = st.text_input(label='Nome:')

def consultar_dados():
    st.title('Consultar clientes')
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.id, item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
    costumerList,
    columns=['Id', 'Nome', 'Idade', 'Profissão'])

    st.table(df)

def inserir():
    st.title('Incluir cliente')

    # Criando formulário para o include
    # A key é o nome do formulário
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira o seu nome")
        input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
        input_occupation = st.selectbox("Selecione sua profissão", 
                                        ["Desenvolvedor",
                                        "Músico", 
                                        "Designer",
                                        "Professor"])
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        cliente.id = uuid.uuid1()
        cliente.nome = input_name
        cliente.idade = input_age
        cliente.profissao = input_occupation

        ClienteController.IncluirCliente(cliente= cliente)
        st.success('Cliente adicionado com sucesso!')

def exibir_menu():
    st.sidebar.title('Menu')
    opcao = st.sidebar.selectbox(options=['Incluir', 'Alterar', 'Excluir', 'Consultar'], label='Opções')

    if opcao == 'Consultar':
        consultar_dados()
    elif opcao ==  'Incluir':
        inserir()
    elif opcao == 'Alterar':
        alterar_dados()


exibir_menu()