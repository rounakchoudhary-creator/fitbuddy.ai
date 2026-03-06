import google.generativeai as genai

# Replace with your Gemini API key
genai.configure(api_key="AIzaSyCr-CZuG3JIB8zFEjeqxcum2hCWIVsLmVg")

model = genai.GenerativeModel("gemini-pro")

def generate_plan(user):

    prompt = f"""
Create a structured 7 day workout plan.

Age: {user.age}
Weight: {user.weight}
Goal: {user.goal}
Intensity: {user.intensity}

Return a clear day-wise workout routine.
"""

    response = model.generate_content(prompt)

    return response.text


def nutrition_tip(goal):

    prompt = f"Give one short nutrition or recovery tip for {goal}"

    response = model.generate_content(prompt)

    return response.text
