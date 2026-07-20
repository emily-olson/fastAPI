from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# this defines the JSON format of our object that the client will send, so that our server knows what to expect when we POST a Thing
class Thing(BaseModel):
    name: str
    price: int


# so this is a decorator of fastapi package. when the app sees a GET request, it will run the code defined below (read_root function).
# the decorator NEEDS the function def
@app.get("/")
def read_root():
    # this returns a python dictionary, which fastapi auto turns into JSON (what HTTP payloads are often in)
    return {"message": "Hi this is Emily's tiny fastAPI server!"}


@app.get("/health")
def get_health():
    return {"status": "ok"}


# this endpoint is also a GET but it requires a parameter. so you can do localhost/8000/items/9 but NOT localhost/8000/items
# the item_id parameter must be an integer or it doesnt work
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"id": item_id, "name": "emily"}


# this item also a GET, but now the parameters are optional! if none passed in, it uses default values. if we do want to pass
# in a parameter, we must use the ?, so it looks like localhost/search?q=banana"
@app.get("/search")
def search(q: str = "", limit: int = 10):
    return {"query": q, "limit": limit, "results": ["apple", "banana"]}


# this is a POST endpoint, so when we call it by visiting this URL, we send a POST request to create data. that means the client
# must send data, as a JSON of the thing we want to create. in this case, we've defined a JSON body to expect from the client
# called Thing
@app.post("/items")
def create_item(item: Thing):
    return {"message": f"a thing with the name {item.name} was created", "item": item}
