Resumen Simple:

🚢 Predicción de Tiempos de Operación Portuaria

Este proyecto ayuda a predecir cuánto tiempo tardará un barco comercial en completar sus operaciones en el puerto de Mazatlán.

En un puerto, no saber cuánto tiempo ocupará cada barco puede causar esperas, pérdidas de dinero y mala organización. Con este proyecto, usamos datos históricos de barcos y un modelo de inteligencia artificial para estimar ese tiempo de manera precisa.

El modelo final puede decir, por ejemplo, que un barco tardará aproximadamente 12 horas, con un margen de error de ±3.5 horas. Esto permite al puerto planificar muelles, personal y operaciones de forma eficiente.

Tecnologías usadas: Python, Machine Learning, Flask y Streamlit para la app web.

En resumen: transforma la incertidumbre de los tiempos de operación en información útil para tomar decisiones rápidas y seguras.


Proyecto completo:

🚢 Predicción de Tiempos de Operación Portuaria - Puerto de Mazatlán

Este proyecto utiliza Machine Learning para predecir el número de horas que un buque comercial tardará en completar sus operaciones en puerto. Su objetivo es transformar la incertidumbre logística en una ventaja estratégica, permitiendo una planificación de recursos y muelles más eficiente.

Los datos se obtuvieron de datos.gob.mx: [Reporte de embarcaciones](https://datos.gob.mx/dataset/reporte_embarcaciones)

📊 Objetivo

En la logística portuaria, el tiempo es el recurso más crítico. La incapacidad de predecir con precisión cuánto tiempo un buque ocupará un muelle genera costos masivos:

Congestión: Buques esperando en el mar.

Costos de personal: Turnos de trabajo mal asignados.

Ineficiencia: Muelles vacíos o sobrecargados.

Este proyecto analiza datos históricos de tráfico (Ene-Jun 2025) y construye un modelo predictivo que estima el tiempo de operación basándose en las características del buque.

🧰 Tecnologías utilizadas

Análisis y manipulación de datos: pandas, numpy

Modelado y preprocesamiento: scikit-learn

Aplicación web: Flask y Streamlit (para pruebas interactivas)

Persistencia del modelo: joblib

Visualización: matplotlib, seaborn

🔄 Flujo del Proyecto

Análisis Exploratorio (EDA)

Detectamos que el puerto operaba a "dos velocidades":

Flota comercial: operaciones rápidas y predecibles.

Flota atunera: operaciones atípicas y extremadamente largas (300–700+ horas).

Limpieza y Segmentación

Se eliminan registros de atuneros y se corrigen errores de captura.

Solo se modela la flota comercial.

Ingeniería de Características (Feature Engineering)
Se crearon dos características nuevas:

densidad_carga = toneladas / (eslora * manga)

eficiencia_carga = toneladas / calado_maximo

Modelado y Optimización

Se probó un RandomForestRegressor optimizado con GridSearchCV.

Las variables cajas_40 y cajas_20 resultaron irrelevantes (<1% importancia), por lo que fueron eliminadas para simplificar el modelo.

Resultados

MAE (Error Absoluto Medio): 3.52 horas

R²: 0.61

El modelo permite pasar de una incertidumbre de días a una ventana de planificación de ±3.5 horas.

🔑 Importancia de las Características
Característica	Importancia (%)
densidad_carga	22.4
eficiencia_carga	21.4
toneladas	16.6
eslora	16.1
tipo_embarcacion_transbordador	6.1


🚀 Cómo ejecutar la aplicación Flask

Clonar el repositorio:

git clone https://github.com/angelbvdev/dataEmbarcaciones.git

cd dataEmbarcaciones/flask_app


Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../requirements.txt


Ejecutar la app Flask:

python app.py


Abrir el navegador en:

http://localhost:5000

🔍 Cómo ejecutar la app Streamlit de pruebas
cd ../7_dashboard
streamlit run app.py

📄 Licencia

Este proyecto está bajo Licencia MIT.
