import numpy as np
import joblib
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")))

# Получаем пути из окружения с резервными вариантами
CSV_PATH = os.getenv("CSV_PATH", "./Cell output 2 [DW].csv")
MODEL_PATH = os.getenv("MODEL_PATH", "../models/model.joblib")

# Нормализуем пути относительно расположения модуля
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
csv_path = CSV_PATH
if not os.path.isabs(csv_path):
    csv_path = os.path.abspath(os.path.join(base_dir, CSV_PATH))

if not os.path.exists(csv_path):
    # альтернативная попытка: соседняя директория проекта
    alt = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "task_3", os.path.basename(CSV_PATH)))
    if os.path.exists(alt):
        csv_path = alt

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV не найден: {csv_path}")

df = pd.read_csv(csv_path)

# Проверяем наличие ожидаемых столбцов
expected = ["feature_1", "feature_2", "feature_3", "feature_4", "feature_5", "target"]
missing = [c for c in expected if c not in df.columns]
if missing:
    raise ValueError(f"Отсутствуют столбцы в CSV: {missing}")

feature_names = [f"feature_{i+1}" for i in range(5)]
X = df[feature_names].astype(float).reset_index(drop=True)
y = df["target"].astype(float).reset_index(drop=True)

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=796695)

# Загрузка модели по пути из .env
model_path = MODEL_PATH
if not os.path.isabs(model_path):
    model_path = os.path.abspath(os.path.join(base_dir, MODEL_PATH))

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found: {model_path}")

model = joblib.load(model_path)

# Расчет коэффициента детерминации R² на тестовой выборке
y_pred_test = model.predict(X_test)
r2 = r2_score(y_test, y_pred_test)


def predict(features: list[float]) -> float:
    """
    Функция для получения предсказания модели на основе входных признаков
    Args:
        features: Список из 5 числовых признаков
    Returns:
        prediction: Предсказанное значение (float)
    """
    X = np.array([list(map(float, features))])
    
    # Получение предсказания модели
    y_pred = model.predict(X)
    return float(y_pred[0])