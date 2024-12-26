import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

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
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.profissao = input_occupation

    try:
        ClienteController.IncluirCliente(cliente= cliente)
    except:
        st.error('Erro ao adicionar novo cliente')
        
    st.success('Cliente adicionado com sucesso!')