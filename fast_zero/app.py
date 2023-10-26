from fastapi import FastAPI

# uvicorn fast_zero.app:app --reload

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}

