from fastapi import FastAPI
from fast_zero.userSchema import UserSchema

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=201)
def create_user(user: UserSchema):
    return user