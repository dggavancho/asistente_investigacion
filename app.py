import streamlit as st
import pandas as pd
from robots.asistente_investigacion import Asisten_Investigacion

asistente_investigacion = Asisten_Investigacion(1,0,8000)

# App title
st.title("Asistente de Investigación")

# Text area
tema_de_investigacion = st.text_area("Descripción del tema de investigación:")

# Text area
caracteristicas_clave = st.text_area("Características clave del estudio:")

# File uploader for Excel
uploaded_file = st.file_uploader("Sube los abstract de los resultados de búsqueda", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    list_dict_input = [
        {
            'tema_de_investigacion':tema_de_investigacion,
            'caracteristicas_clave':caracteristicas_clave,
            'abstract':abstract,
        }
        for abstract in df.Abstract
    ]
    
    
    st.write("### Resultados:")
    st.dataframe(pd.concat(
        [
        df,
        pd.DataFrame(asistente_investigacion.map_invoke(list_dict_input))[['relevancia','razones']]
        ],
        axis=1
    ))
