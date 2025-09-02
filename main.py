from fastapi import Body, FastAPI
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str

@app.get("/")
def root():
    return {"message": "Welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {'data': "This is your psots"}


@app.post('/create_post')
def create_post(payload: dict= Body(...)):
    print(payload)
    return {"new_msg": f"title: {payload['title']} content: {payload['content']}"}