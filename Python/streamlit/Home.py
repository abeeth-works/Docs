import streamlit as sl
import pandas as pd

dataframe = pd.read_excel('videogamesales.xlsx')
sl.write(dataframe)
