from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #this is a default option which will provide true all time
    rating: Optional[int] = None #this is an optional field

@app.get("/")
def root():
    return {"message": "Welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {'data': "This is your psots"}


@app.post('/create_post')
def create_post(new_post: Post):
    print(new_post)
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    print(new_post.rating)
    print(new_post.dict()) #this will convert the pydantic model to a dictionary
    return {"message": "Post created successfully"}