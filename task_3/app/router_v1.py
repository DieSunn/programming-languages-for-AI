import fastapi
import ml_tools


# Версионированный роутер v1
router_v1 = fastapi.APIRouter(prefix="/api/v1", tags=["v1"])

@router_v1.get(
    "/ping",
    summary="Проверка состояния (ping)",
    description="Простейшая проверка работоспособности сервера. Возвращает JSON с полем message='ok'.",
)
async def ping():
    """
    Проверка работоспособности сервера.
    Возвращаемое значение:
        {"message": "ok"}
    """
    return {"message": "ok"}


@router_v1.post(
    "/prediction",
    summary="Предсказание",
    description=(
        "Получить предсказание модели по пяти числовым признакам.\n"
        "Параметры (как query или form в POST): feature_1, feature_2, feature_3, feature_4, feature_5.\n"
        "Возвращает числовое предсказание (float)."
    ),
)
async def get_prediction(
    feature_1: float,
    feature_2: float,
    feature_3: float,
    feature_4: float,
    feature_5: float,
):
    """
    Получает пять числовых признаков и возвращает предсказание модели.

    Аргументы:
        feature_1..feature_5 (float): входные признаки

    Ответ:
        float: предсказанное значение
    """
    return ml_tools.predict([feature_1, feature_2, feature_3, feature_4, feature_5])


@router_v1.get(
    "/model_info",
    summary="Информация о модели",
    description="Возвращает метрики и основную информацию о загруженной модели (например, r2_score).",
)
async def model_info():
    """
    Возвращает информацию о модели:
        {"r2_score": <значение>}
    """
    return {
        "r2_score": ml_tools.r2,
    }