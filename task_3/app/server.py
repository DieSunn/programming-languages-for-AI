import fastapi
import ml_tools
from router_v1 import router_v1


app = fastapi.FastAPI(
    title="API линейной регрессии",
    description="API для проверки работоспособности линейной регрессии.",
    version="1.0"
)


@app.get(
    "/",
    summary="Корневой эндпоинт",
    description="Приветственное сообщение. Можно использовать для быстрой проверки доступности API.",
)
async def root():
    """
    Корневой эндпоинт API.
    Возвращаемое значение:
        {"message": "Hello, World!"}
    """
    return {"message": "Hello, World!"}


# Регистрируем версионированный роутер в приложении
app.include_router(router_v1)