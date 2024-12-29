import streamlit as st
import Controllers.ClienteController as ClienteController
import pandas as pd

def consultar_dados():
    st.title('Consultar clientes')
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.id, item.nome, item.idade, item.profissao])

    df = pd.DataFrame(
    costumerList,
    columns=['Id', 'Nome', 'Idade', 'Profissão'])

    st.table(df)