from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True 
    rating: Optional[int] = None 


my_posts = [{"title":"title of post 1", "content": "content of post 1","id": 1},{"title":"favourite food", "content": "I like pizza","id": 2}]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post
        

def find_indexpost(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def root():
    return {"message": "Welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {'data': my_posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0,1000000)
    my_posts.append(post_dict) 
    return {"data": post_dict}

@app.get("/latest")
def get_latest_post():
    return {"detail": my_posts[-1]}



@app.get("/posts/{id}")
def get_post(id: int):
    post =find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post details": post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    index = find_indexpost(id)
    my_posts.pop(index)
    return{"message": "post was successfully deleted"}
