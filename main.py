from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my api!!"}

@app.get("/posts")
def get_posts():
    return {'data': "This is your psots"}


@app.post('/create_post')
def create_post():
    return {"Post created successfully"}