🚢 Predicción de Tiempos de Operación Portuaria en el puerto de Mazatlan
Datos obtenidos de https://datos.gob.mx/dataset/reporte_embarcaciones
Este proyecto utiliza Machine Learning para predecir el número de horas que un buque comercial tardará en completar sus operaciones en puerto. El objetivo es transformar la incertidumbre logística en una ventaja estratégica, permitiendo una planificación de recursos y muelles más eficiente.

El modelo final es una aplicación web interactiva construida con Streamlit, capaz de predecir tiempos operativos con un Error Absoluto Medio (MAE) de ~3.52 horas.

Vistazo a la Aplicación Final (Streamlit)
En la carpeta numero 8 Pruebas

El Problema
En la logística portuaria, el tiempo es el recurso más crítico. La incapacidad de predecir con precisión cuánto tiempo un buque ocupará un muelle genera costos masivos:

Congestión: Buques esperando en el mar.

Costos de Personal: Turnos de trabajo mal asignados.

Ineficiencia: Muelles vacíos o sobrecargados.

Este proyecto aborda el problema analizando datos históricos de tráfico (Ene-Jun 2025) para construir un modelo predictivo que estima el tiempo de operación basándose en las características del buque.

Tech Stack (Tecnologías Usadas)
Análisis y Manipulación: pandas, numpy

Modelado y Preprocesamiento: scikit-learn

Aplicación Web: streamlit

Persistencia del Modelo: joblib

Visualización: matplotlib, seaborn

 Metodología y Flujo del Proyecto
Este proyecto no fue solo entrenar un modelo; fue un ciclo completo de descubrimiento y refinamiento.

1. Análisis Exploratorio (EDA)
El análisis inicial reveló un hallazgo clave: el puerto operaba a "dos velocidades".

Una flota comercial (cargueros, petroleros) con operaciones rápidas y predecibles.

Una flota atunera con un comportamiento completamente atípico: estadías extremadamente largas (300-700+ horas) que no se correlacionaban con su tamaño.

2. Limpieza y Segmentación
Se tomó la decisión estratégica de segmentar el análisis. El modelo se enfocaría exclusivamente en la flota comercial para predecir sus operaciones. La flota atunera se considera un problema de negocio separado.

Se eliminaron los registros de atuneros.

Se corrigieron errores de captura (ej. un calado_maximo imposible de 31m) y categorías duplicadas.

3. Ingeniería de Características (Feature Engineering)
Para darle al modelo una "intuición" física, se crearon dos características nuevas, que resultaron ser las más importantes:

densidad_carga: toneladas / (eslora * manga)

eficiencia_carga: toneladas / calado_maximo

4. Modelado y Optimización
Se probó un RandomForestRegressor por su capacidad para capturar relaciones complejas. Se utilizó GridSearchCV para encontrar la combinación óptima de hiperparámetros, optimizando para el Error Absoluto Medio.

5. Interpretación y Refinamiento (El Hallazgo Clave)
El análisis de importancia (feature_importance) reveló un descubrimiento sorprendente:

Las variables cajas_40 y cajas_20 (cantidad de contenedores) eran casi irrelevantes (menos del 1% de importancia).

El modelo determinó que esta información ya estaba "incluida" en variables más potentes como toneladas y densidad_carga.

Acción: El modelo final fue re-entrenado sin las variables de contenedores, resultando en un modelo más ligero, rápido y más preciso.

Resultados y Hallazgos
Modelo Final
Modelo: RandomForestRegressor (simplificado)

Error Absoluto Medio (MAE): 3.52 horas.

R-cuadrado (R²): 0.61 (El modelo explica el 61% de la variabilidad en los tiempos).

Un error de ~3.5 horas no es un "mal modelo"; es un resultado excelente. Transforma una incertidumbre que podía ser de días (vimos operaciones de 8 a 150 horas) en una ventana de planificación precisa, permitiendo al puerto pasar de ser reactivo a proactivo.

Importancia de las Características
Las características más decisivas para el modelo fueron:

densidad_carga (22.4%): La característica creada fue la más importante.

eficiencia_carga (21.4%): La segunda característica creada.

toneladas (16.6%)

eslora (16.1%)

tipo_embarcacion_transbordador (6.1%): El modelo aprendió que ser un transbordador reduce significativamente el tiempo.

Cómo Usar este Proyecto
1. Requisitos Previos
Asegúrate de tener Python 3.8+ instalado.

2. Clonar el Repositorio
Bash

git clone https://github.com/angelbvdev/dataEmbarcaciones.git
cd dataEmbarcaciones
3. Crear un Entorno Virtual e Instalar Dependencias
Bash

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
(Asegúrate de tener un archivo requirements.txt con pandas, scikit-learn, streamlit y joblib)

4. Ejecutar la Aplicación Streamlit

Entra en la carpeta 7_dashboard 
Asegúrate de que el modelo entrenado (modelo_final.pkl) esté en la misma carpeta.

Bash

streamlit run app.py
¡Abre tu navegador en http://localhost:8501 y comienza a hacer predicciones!

📄 Licencia
Este proyecto está bajo la Licencia MIT.
