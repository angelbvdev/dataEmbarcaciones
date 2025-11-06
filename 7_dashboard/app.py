import streamlit as st
import pandas as pd
import joblib

# 1. Cargar el modelo FINAL y SIMPLIFICADO
# Este es el modelo que tiene el MAE de 3.52 y no usa las 'cajas'
try:
    modelo = joblib.load("modelo_final.pkl")
except FileNotFoundError:
    st.error("Error: No se encontró el archivo 'modelo_final_simplificado.pkl'.")
    st.stop() # Detiene la ejecución si no encuentra el modelo

st.title("🚢 Predicción de Horas de Operación")
st.markdown("Estima el tiempo que un buque comercial (no atunero) tardará en completar sus operaciones en puerto.")

# --- Sección de Inputs del Usuario ---
st.header("Datos del Buque")

# 2. Inputs del usuario
tipos_conocidos = [
    'transbordador', 'carguero', 'petrolero', 'acero', 
    'car-carrier', 'contenedor'
]
tipo_embarcacion = st.selectbox(
    "Tipo de Embarcación", 
    options=tipos_conocidos
)

# 3. Mejora: Usar columnas para un layout más limpio
col1, col2, col3 = st.columns(3)

with col1:
    eslora = st.number_input("Eslora (m)", min_value=20.0, max_value=300.0, value=150.0)
with col2:
    manga = st.number_input("Manga (m)", min_value=5.0, max_value=50.0, value=25.0)
with col3:
    calado_maximo = st.number_input("Calado Máximo (m)", min_value=3.0, max_value=20.0, value=10.0)

toneladas = st.number_input("Tonelaje (t)", min_value=100.0, max_value=50000.0, value=5000.0)


# --- Lógica de Predicción ---
if st.button("Estimar Horas"):
    
    # 4. Crear las features derivadas (tu lógica era perfecta)
    epsilon = 1e-6 
    densidad_carga = toneladas / ((eslora * manga) + epsilon)
    eficiencia_carga = toneladas / (calado_maximo + epsilon)

    # 5. Crear el DataFrame de entrada para el modelo
    input_data = pd.DataFrame({
        'toneladas': [toneladas],
        'eslora': [eslora],
        'calado_maximo': [calado_maximo],
        'tipo_embarcacion': [tipo_embarcacion],
        'densidad_carga': [densidad_carga],
        'eficiencia_carga': [eficiencia_carga]
    })

    # 6. Realizar la predicción
    try:
        prediccion = modelo.predict(input_data)[0]
        
        # 7. Mejora: Mostrar el resultado con st.metric
        st.subheader("Resultado de la Predicción")
        st.metric(
            label="Tiempo Estimado de Operación",
            value=f"{prediccion:.2f} horas",
            help="Predicción basada en el modelo de RandomForest (MAE: 3.52 hrs)"
        )
        
        # Explicación del rango
        st.info(f"Basado en el error promedio (MAE) de 3.52 horas, puedes esperar que la operación real tome entre **{(prediccion - 3.52):.2f}** y **{(prediccion + 3.52):.2f}** horas.")
    
    except Exception as e:
        st.error(f"Error al predecir: {e}")