import uuid
import streamlit as st
import Controllers.ClienteController as ClienteController
import pandas as pd

def buscar_por_id(deletar_id):
    costumerList = []

    for item in ClienteController.SelecionarPorId(deletar_id):
        costumerList.append([item.id, item.nome, item.idade, item.profissao])

    if costumerList == []:
        st.error('Não foi encontrado cliente cadastrado com esse Id')
    else:
        df = pd.DataFrame(
        costumerList,
        columns=['Id', 'Nome', 'Idade', 'Profissão'])

        st.table(df)

def excluir_dados():
    st.title('Excluir cliente cadastrado')

    id = st.text_input(label='Id:')
    id.replace(' ', '')

    if id != '':
        deletar_id = uuid.UUID(id)

        buscar_por_id(deletar_id)        

        confirmar_delete = st.button(label='Deletar registro')

        if confirmar_delete:
            try:
                ClienteController.DeletarPorId(deletar_id)
                st.success('O registro foi deletado com sucesso, atualize a página para visualizar o banco.')
            except:
                st.error('Ocorreu um erro na deleção')
        
