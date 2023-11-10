from fastapi import FastAPI
from pydantic import BaseModel


# аннотации типов
# класс с типами данных параметров
class Item(BaseModel):
    value_1: float
    value_2: float
    operation: str


# создаем объект приложения
app = FastAPI()


# функция, которая будет обрабатывать запрос по пути "/"
# полный путь запроса http://127.0.0.1:8000/
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}


# функция-обработчик post запроса с параметрами
@app.post("/calc")
def get_calc(item: Item):
    result = None  # Инициализируем result
    if item.operation == 'addition':
        result = item.value_1 + item.value_2
    elif item.operation == 'difference':
        result = item.value_1 - item.value_2
    elif item.operation == 'division':
        try:
            result = item.value_1 / item.value_2
        except ZeroDivisionError:
            return {"error": "division by zero"}
    elif item.operation == 'multiplication':
        result = item.value_1 * item.value_2
    else:
        return {"error": "Unknown operation"}

    return {"result": result}
