# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 19:50:31 2025

@author: bryan
"""

import streamlit as st
import joblib
import numpy as np

#defino ruta del modelo formato pkl
model_filename = 'modelo_flores.pkl'
#cargamos el modelo pkl
loaded_model = joblib.load(model_filename)


print("Archivo pkl cargado!")


# Configuración de la página
st.set_page_config(page_title="Mi Página con Streamlit", layout="wide")

# Crear el panel lateral
st.sidebar.title("Menú de Páginas")
page = st.sidebar.selectbox("Selecciona una página", ("Inicio", "Prediccion", "Acerca de"))

# Contenido según la opción seleccionada
if page == "Inicio":
    st.title("Inicio")
    st.write("Esta es una aplicacion para predecir la especie de flor según las dimensiones de petalos y sepalos.")

    # Puedes agregar más widgets para la Página 1 aquí
    st.write("Más contenido o gráficos específicos para la Página 1.")

elif page == "Prediccion":
    st.title("Bienvenido a la Prediccion")
    st.write("Esta es la segunda página de tu aplicación.")
    
    
    with st.form(key='flores-pred-form'):
        
                
             
        a = float(st.number_input("sepal length in cm"))
        b = float(st.number_input("sepal width in cm"))
        c = float(st.number_input("petal length in cm"))
        d = float(st.number_input("petal width in cm"))

        btn = st.form_submit_button("predict") 
        
        if btn:
            pred = loaded_model.predict(np.array([a,b,c,d]).reshape(1,-1))
            pred = np.argmax(pred)
            st.subheader(pred)
            
            if pred==0:
                print("Setosa")
                st.image("setosa.jpg")
            elif pred==1:
                print("Versicolor")
                st.image("versicolor.jpg")
            else:
                print("verginca")
                st.image("verginca.jpg")
        
        
    
    
    # Agregar contenido para la Página 2 aquí
    st.write("Más contenido o gráficos específicos para la Página 2.")

else:
    st.title("Bienvenido a Acerca de")
    st.write("Esta es la tercera página de tu aplicación.")

    # Agregar contenido para la Página 3 aquí
    st.write("Más contenido o gráficos específicos para la Página 3.")