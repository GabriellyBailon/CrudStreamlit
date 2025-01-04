import uuid
import streamlit as st
import Controllers.ClienteController as ClienteController
import pandas as pd

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
            with st.form(key="update_cliente"):
                input_name = st.text_input(label="Insira o seu nome")
                input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
                input_occupation = st.selectbox("Selecione sua profissão", 
                                                ["Desenvolvedor",
                                                "Músico", 
                                                "Designer",
                                                "Professor"])
                input_button_submit = st.form_submit_button("Enviar")

                if input_button_submit:
                    # Busca o cliente pelo ID selecionado
                    cliente_atual = costumerList[0]
                    if cliente_atual:
                        # Atualiza os valores
                        if input_name:
                            cliente_atual[1] = input_name
                        if input_age >= 0:
                            cliente_atual[2] = input_age
                        if input_occupation:
                            cliente_atual[3] = input_occupation

                        # Chama o controlador para atualizar
                        ClienteController.AlterarCliente(cliente_atual)