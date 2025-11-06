Conclusiones (De etapa 1-3)

El análisis realizado permitió identificar que el puerto presenta dos perfiles operativos claramente diferenciados, lo que hace indispensable tratarlos como segmentos independientes en cualquier análisis o modelo predictivo.

Por un lado, se encuentra la operación de tráfico comercial de buques mayores, caracterizada por su rapidez, estabilidad y alta frecuencia. Por otro, se observa una operación asociada a la base de flota atunera, compuesta por un grupo reducido de embarcaciones con tiempos de estadía considerablemente más largos y variables.
Esta dualidad define al puerto como un sistema de “dos velocidades”, con dinámicas operativas y logísticas contrastantes.

1. Principales hallazgos

Tráfico predominante: La operación está dominada por embarcaciones de bandera mexicana y de tipo transbordador, que representan la mayoría de los arribos.

Perfil de carga: Los buques de mayor tonelaje promedio corresponden a los tipos petrolero, carguero y car-carrier, con predominio de banderas como Panamá y Filipinas.

Correlación crítica: Se encontró una correlación de 0.99 entre las variables horas_buque_puerto y horas_buque_operacion, lo que indica redundancia entre ambas. Esto refleja que, para la flota comercial, el tiempo en puerto equivale casi completamente al tiempo operativo.

Patrón temporal: Los datos depurados muestran que los meses de febrero y marzo concentraron los picos de actividad (promedios cercanos a 21 horas de operación), mientras que el resto del semestre mantuvo una tendencia más baja y estable (entre 11 y 14 horas).

2. El puerto de dos velocidades

Velocidad 1: Flota comercial (operación estándar)

Tipos: Cargueros, petroleros, transbordadores, car-carriers.

Comportamiento: Alta eficiencia y consistencia; la mayoría de las operaciones se completan en menos de 25 horas.

Características físicas: Buques de gran tamaño (eslora promedio de 140–180 m) con altos tonelajes.

Velocidad 2: Flota atunera (operación extendida)

Tipos: Atuneros.

Comportamiento: Operaciones lentas y variables, con estadías que pueden extenderse por cientos de horas.

Características físicas: Buques de menor tamaño (esloras inferiores a 80 m) y tonelaje reducido.

3. Implicaciones y próximos pasos

Segmentación analítica: Es fundamental separar las embarcaciones atuneras de las comerciales antes de construir modelos predictivos o análisis de desempeño. Los patrones de comportamiento son distintos y deben analizarse por separado.

Calidad y consistencia: La limpieza de datos permitió eliminar registros erróneos (por ejemplo, calados imposibles de 31 m) y unificar categorías duplicadas o incorrectas, generando un conjunto confiable.

Optimización de variables: Dado el alto grado de correlación entre horas_buque_puerto y horas_buque_operacion, una de ellas puede eliminarse en futuros modelos para simplificar el análisis sin pérdida de información.