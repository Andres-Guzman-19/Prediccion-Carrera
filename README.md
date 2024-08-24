<div style="text-align: center;">

# 	:school: Prediccion de carrera

</div>

Este proyecto tiene como objetivo predecir la carrera futura de los estudiantes de ciencias de la computación y analizar cómo diversas variables influyen en su elección de carrera. Los datos utilizados para este análisis fueron obtenidos de [Kaggle](https://www.kaggle.com/datasets/devildyno/computer-science-students-career-prediction)

Para alcanzar este objetivo, se entrenaron cinco modelos de clasificación:
* SVC
* K neighbors classifier
* Gradient Boosting classifier
* Regresion logistica
* Random forest classifier
Además, se realizó un ajuste de hiperparámetros utilizando la biblioteca Optuna. Y para facilitar la realización de nuevas predicciones, se implementó una interfaz interactiva con Gradio, la cual se puede usar con ayuda de [Hugging Face](https://huggingface.co/spaces/Andicia1904/computer-science-students-career-prediction).

<div style="text-align: center;">

## :book: Identificación de las columnas


| Columna | Descripcion |
|-|-|
|Stdent ID| Identificador único para cada estudiante|
|Name|Nombre del estudiante|
|Gender|Género del estudiante|
|Age|Edad del estudiante|
|GPA|Promedio de calificaciones del estudiante|
|Major|Campo de estudio dentro de la informática|
|Interested Domain|Área de interés dentro del campo de la informática|
|Projects|Proyectos destacados completados por el estudiante|
|Python|Nivel de competencia en programación Python|
|SQL|Nivel de competencia en consultas SQL|
|Java|Nivel de competencia en programación Java|
|Carrera futura|Trayectoria profesional prevista o aspiración laboral (variable objetivo)|

</div>

El mejor modelo entrenado fue el Gradient Boosting, con una precisión del 86.1%. Sin embargo, hay oportunidades para mejorar esta métrica evaluando otros algoritmos o ajustando aún más los hiperparámetros.