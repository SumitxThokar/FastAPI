from fastapi import FastAPI
app = FastAPI()

# minimal app - get request

# get - read todo 
@app.get("/todo",tags=['todos'])
async def get_todo()-> dict:
    return {"data":todos}

todos =[
    {"id":"1",
     "Activity":"Wake up early in the morning."
    },
    {
        "id":"2",
        "Activity":"Complete Numerical Method Assignment."
    },
    {
        "id":"3",
        "Activity":"Mail your cv to the X company."
    }
]

# Post route -> create todo
@app.post("/todo",tags=["todos"])
async def add_todo(todo:dict)-> dict:
    todos.append(todo)
    return{
        "data":"Added successfully!"
    }

# Put route -> update todo
@app.put("/todo/{id}",tags=['todos'])
async def update_todo(id:int,body:dict)->dict:
    for todo in todos:
        if int((todo['id']))==id:
            todo['Activity']=body['Activity']
            return {
                "data":f"id {id} has been successfully updated!"
            }
    return {
        "data":f"id {id} was not found!"
    }

@app.delete("/todo/{id}",tags=['todos'])
async def delete_todo(id:int)->dict:
    for todo in todos:
        if int((todo['id']))==id:
            todos.remove(todo)
            return {
                "data":f"todo {id} has been deleted."
            }
    return {
        "data":f"todo {id} was not found."
    }