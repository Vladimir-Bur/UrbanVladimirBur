from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def Get_User():
    return users

@app.post('/user/{username}/{age}')
async def Add_User(username, age):
    new_key = str(int(max(users, key=int)) + 1)
    users[new_key] = f'Имя: {username}, возраст: {age}'
    return f'User {new_key} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def Update_User(user_id, username, age):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def Delete_User(user_id):
    users.pop(user_id)
