from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load the marks data (replace 'marks.json' with your filename)
with open("marks.json") as f:
    student_data = json.load(f)

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_data.get(name, None) for name in names]
    return {"marks": marks}
