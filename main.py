from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    title: str
    completed: bool

tasks = []

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    return tasks[task_id]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    tasks[task_id] = task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    del tasks[task_id]
    return {"detail": "Task deleted."}
