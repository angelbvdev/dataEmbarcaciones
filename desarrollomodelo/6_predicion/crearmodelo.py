import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# 1️ Cargar dataset limpio (solo buques comerciales)
df = pd.read_csv("embarcaciones_comercial.csv")

# 2️ Crear features derivadas
df['densidad_carga'] = df['toneladas'] / (df['eslora'] * df['manga'])
df['eficiencia_carga'] = df['toneladas'] / df['calado_maximo']

# 3️ Variables predictoras y objetivo
X = df[['cajas_40', 'cajas_20', 'toneladas', 'eslora', 'calado_maximo', 
        'tipo_embarcacion', 'densidad_carga', 'eficiencia_carga']]
y = df['horas_buque_operacion']

# 4️Separar variables numéricas y categóricas
numeric_features = ['cajas_40', 'cajas_20', 'toneladas', 'eslora', 'calado_maximo',
                    'densidad_carga', 'eficiencia_carga']
categorical_features = ['tipo_embarcacion']

# 5️Pipeline de preprocesamiento
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# 6️ Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7️ Crear pipeline completo con RandomForest
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(
        n_estimators=200, max_depth=10, random_state=42
    ))
])

# 8️ Entrenar modelo
pipeline.fit(X_train, y_train)

# 9️ Evaluación
y_pred = pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"¡Modelo entrenado con RandomForest!")
print(f"MAE (horas promedio): {mae:.2f}")
print(f"R²: {r2:.2f}")

# 10 Guardar modelo
joblib.dump(pipeline, "modelo_prediccion_horas_buque.pkl")
print("Modelo guardado como 'modelo_prediccion_horas_buque.pkl'")
