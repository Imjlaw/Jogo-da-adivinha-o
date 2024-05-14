import pandas as pd # Manipular os dados
import streamlit as st # Construir os DashBoards
import plotly.express as px # Construir os gráficos

st.set_page_config(layout="wide")


df = pd.read_csv("Aluno_Contratação.csv", sep=",", decimal=".")

df

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
qtd = len(df['gender'])

gender = px.bar(df, x="gender", color="hsc_s", title="Gêneros")
col1.plotly_chart(gender)

prof = px.bar(df, x="gender", color="degree_t", title="Gêneros")
col1.plotly_chart(prof)