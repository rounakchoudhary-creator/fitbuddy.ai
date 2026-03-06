from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

from models import UserInput
from ai_service import generate_plan, nutrition_tip
import database

app = FastAPI()

templates = Jinja2Templates(directory="templates")

conn = sqlite3.connect("fitbuddy.db", check_same_thread=False)
cursor = conn.cursor()


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/generate-plan")
def generate(user: UserInput):

    plan = generate_plan(user)
    tip = nutrition_tip(user.goal)

    cursor.execute(
        "INSERT INTO users(name,age,weight,goal,intensity,plan) VALUES(?,?,?,?,?,?)",
        (user.name, user.age, user.weight, user.goal, user.intensity, plan)
    )

    conn.commit()

    return {
        "workout_plan": plan,
        "nutrition_tip": tip
    }