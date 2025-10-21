import gradio as gr
import numpy as np
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Генерация синтетических данных для демонстрации
X, y = make_regression(n_samples=400, n_features=5, n_informative=3, noise=50, random_state=796695)
feature_names = [f"feature_{i+1}" for i in range(5)]
X = pd.DataFrame(X, columns=feature_names)  # Преобразование в DataFrame для удобства
y = pd.Series(y, name="target")  # Целевая переменная

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=796695)

# Загрузка предварительно обученной модели
model = joblib.load('model.pkl')

# Расчет коэффициента детерминации R² на тестовой выборке
y_pred_test = model.predict(X_test)
r2 = r2_score(y_test, y_pred_test)

# Определение наиболее важного признака по модулю коэффициентов регрессии
feature_importance = abs(model.coef_)
most_important_idx = np.argmax(feature_importance)
most_important_feature = feature_names[most_important_idx]

# Получаем топ x`3 важных признака
top_features_idx = np.argsort(feature_importance)[-3:][::-1]
top_features = [feature_names[i] for i in top_features_idx]

# Создание уравнения регрессии в формате LaTeX
coef_rounded = [f"{coef:.2f}" for coef in model.coef_]  # Округление коэффициентов
intercept_rounded = f"{model.intercept_:.2f}"  # Округление свободного члена
equation = f"y = {intercept_rounded}"
for i, coef in enumerate(coef_rounded):
    equation += f" + ({coef})x_{i+1}"

def create_scatter_plot(X_input):
    """
    Создание нескольких диаграмм рассеяния для топ-3 важных признаков
    Args:
        X_input: входные данные для предсказания
    Returns:
        plt: объект графика matplotlib
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    fig.suptitle('Диаграммы рассеяния: Важнейшие признаки vs Целевая переменная')
    
    for idx, (ax, feature_idx, feature_name) in enumerate(zip(axes, top_features_idx, top_features)):
        # Отображение точек обучающей выборки
        sns.scatterplot(data=pd.DataFrame({'x': X_train[feature_name], 'y': y_train}),
                       x='x', y='y', alpha=0.5, label='Обучающие данные', ax=ax)
        
        # Добавление линии регрессии
        sns.regplot(data=pd.DataFrame({'x': X_train[feature_name], 'y': y_train}),
                   x='x', y='y', scatter=False, color='blue', 
                   line_kws={'label': 'Линия регрессии'}, ax=ax)
        
        # Отображение точки введенных пользователем данных
        ax.scatter(X_input[feature_idx], model.predict([X_input]), 
                  color='red', s=100, label='Ваши данные')
        
        ax.set_xlabel(feature_name)
        ax.set_ylabel('Целевая переменная')
        ax.legend()
    
    plt.tight_layout()
    return plt

def predict(*features):
    """
    Функция для предсказания значения целевой переменной
    Args:
        *features: набор признаков от пользователя
    Returns:
        tuple: предсказанное значение и график
    """
    X = np.array([list(map(float, features))])
    
    # Получение предсказания модели
    y_pred = model.predict(X)
    
    # Создание визуализации
    fig = create_scatter_plot(X[0])
    
    return float(y_pred[0]), fig

# Создание веб-интерфейса с помощью Gradio
iface = gr.Interface(
    fn=predict,
    inputs=[gr.Number(label=name) for name in feature_names],  # Поля ввода для каждого признака
    outputs=[
        gr.Number(label="Предсказанное значение"),
        gr.Plot(label="Визуализация")
    ],
    title="Линейная регрессия - Предсказание",
    description=f"Качество модели: R² = {r2:.3f}",
    article=f"""
    ### Уравнение модели:
    $${equation}$$
    
    Где x_1 ... x_{len(feature_names)} - входные признаки.
    Наиболее важный признак: {most_important_feature}
    """
)

if __name__ == "__main__":
    iface.launch()  # Запуск веб-интерфейса