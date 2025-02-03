from fastapi import FastAPI, Path

# 1. Создаем приложение(объект) FastAPI
app = FastAPI()

# 2. Создаем маршрут к главной странице
@app.get("/")
async def Main_Page():
    return {"message": "Главная страница"}

# 3. Создаем маршрут к странице администратора
@app.get("/user/admin")
async def Admin_Page() -> dict:
    return {"message": "Вы вошли как администратор"}

# 4. Создаем маршрут к страницам пользователей, используя параметр в пути
@app.get("/user/{user_id}")
async def User_Page(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='71')) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# 5. Создаем маршрут к страницам пользователей передавая данные в адресной строке
@app.get("/user/{username}/{age}")
async def User_Info(username: str = Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser'),
                    age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
