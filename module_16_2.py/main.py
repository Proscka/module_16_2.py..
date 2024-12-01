from fastapi import FastAPI,Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def welcome()->str:
    return (f"Главная страница")

@app.get('/user/admin')
async def administrator()->str:
    return (f"Вы вошли как администратор")

@app.get('user/{user_id}')
async def user_number(user_id: Annotated[int, Path(ge=1,le=100,description="Enter User ID")]):
    return (f"Вы вошли как пользователь № {user_id}")

@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_leght=5, max_leght=20, description="Enter username")],
                    age: Annotated[int, Path(ge=18,le=120,discription="Enter age")]):
    return (f"Информация о пользователе. Имя:{username}, Возраст:{age}")
