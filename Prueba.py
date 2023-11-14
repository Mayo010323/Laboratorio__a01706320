import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo
data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100)
})

# Crear una aplicación Streamlit simple
st.title('Gráfico con Streamlit')

# Agregar una gráfica al cuerpo de la aplicación
st.line_chart(data.set_index('x'))

# Puedes personalizar la gráfica según tus necesidades
# Por ejemplo, agregar un título y etiquetas de ejes
plt.plot(data['x'], data['y'])
plt.title('Gráfico con Matplotlib')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar la gráfica en Streamlit
st.pyplot(plt)
