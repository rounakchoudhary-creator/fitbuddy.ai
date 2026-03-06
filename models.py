from pydantic import BaseModel

class UserInput(BaseModel):
    name: str
    age: int
    weight: int
    goal: str
    intensity: str

class Feedback(BaseModel):
    user_id: int
    feedback: str