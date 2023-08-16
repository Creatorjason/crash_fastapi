from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1:{
        "name": "Jason",
        "age": 22,
        "occupation": "Tinkerer",
    },
    2:{
        "name":"Ayoleyi",
        "age":23,
        "occupation":"Programmer",
    }
}
# we use the Path attribute to add descriptions to our path params




# we create a data model similar to structs in Golang
class Student(BaseModel):
    name : str
    age: int
    occupation : str


class UpdateStudent(BaseModel):
    name : Optional[str] = None
    age: Optional[str] = None
    occupation : Optional[str] = None

@app.get("/")
def index():
    return {"first":"Jason"}


@app.get("/api/get-students/{student_id}")
def get_students(student_id: int):
    return students[student_id]


# using query parameters

@app.get("/api/get-student")
def get_student(*, name: Optional[str] = None, occupation: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


# request body and the post method



@app.post("/api/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Entity already exist "}
    students[student_id] = student
    return students[student_id]



# using the PUT method

@app.put("/api/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student data not found"}

    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age  != None:
        students[student_id]["age"] = student.age
    if student.occupation != None:
        students[student_id]["occupation"] = student.occupation
    
    students[student_id] = student
    return students[student_id] 