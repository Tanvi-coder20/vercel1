from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data (array of objects)
with open("marks.json") as f:
    data = json.load(f)

# Convert list of dicts into dict for fast lookup
student_data = {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_data.get(name, None) for name in names]
    return {"marks": marks}
