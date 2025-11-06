import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib
import warnings

warnings.filterwarnings('ignore')

# 1️ Cargar dataset
df = pd.read_csv("embarcaciones_comercial.csv")

# 2️ Crear features derivadas
df['densidad_carga'] = df['toneladas'] / (df['eslora'] * df['manga'])
df['eficiencia_carga'] = df['toneladas'] / df['calado_maximo']

# 3️ Variables predictoras y objetivo (¡SIMPLIFICADAS!)
X = df[['toneladas', 'eslora', 'calado_maximo', 
        'tipo_embarcacion', 'densidad_carga', 'eficiencia_carga']] # Sin 'cajas'
y = df['horas_buque_operacion']

# 4️ Separar variables (¡SIMPLIFICADAS!)
numeric_features = ['toneladas', 'eslora', 'calado_maximo',
                    'densidad_carga', 'eficiencia_carga'] # Sin 'cajas'
categorical_features = ['tipo_embarcacion']

# 5️ Pipeline de preprocesamiento (sin cambios)
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

# 7️ Crear pipeline final con los *mejores* parámetros
# Usamos la configuración que GridSearchCV encontró
best_params = {
    'n_estimators': 300,
    'max_depth': 10,
    'max_features': 'sqrt',
    'min_samples_leaf': 1,
    'random_state': 42
}

final_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(**best_params))
])

# 8️ Entrenar modelo final
print("Entrenando el modelo final simplificado...")
final_pipeline.fit(X_train, y_train)

# 9️ Evaluación
y_pred = final_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Resultados del Modelo Final Simplificado ---")
print(f"MAE (horas promedio): {mae:.2f}")
print(f"R²: {r2:.2f}")

# 10 Guardar modelo
joblib.dump(final_pipeline, "modelo_final_simplificado.pkl")
print("Modelo final guardado como 'modelo_final_simplificado.pkl'")