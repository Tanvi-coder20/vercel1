from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Embedded student marks data
data = [
    {"name":"d40Yp","marks":45},{"name":"M5to5","marks":38},{"name":"QP","marks":13},{"name":"QKsrOk50","marks":98},
    {"name":"isMOM","marks":50},{"name":"lBJeoV3Q","marks":43},{"name":"H","marks":17},{"name":"NfHj9KeqGu","marks":74},
    {"name":"yLB6NE","marks":27},{"name":"fL","marks":6},{"name":"u","marks":59},{"name":"u9d","marks":75},
    {"name":"kt6pnoMn","marks":83},{"name":"cNa","marks":96},{"name":"nK60jYR3a","marks":82},{"name":"ijYtbiGB","marks":0},
    {"name":"UD","marks":9},{"name":"U7Nbfr","marks":67},{"name":"iw","marks":86},{"name":"OlhgwJXuBk","marks":74},
    {"name":"pZYAGtW","marks":73},{"name":"FHgZuZCV9","marks":39},{"name":"5sklG","marks":7},{"name":"Qcf","marks":28},
    {"name":"bXJ","marks":15},{"name":"hbrpCpJ","marks":55},{"name":"PVASw6OQq","marks":44},{"name":"ERwfuVL","marks":79},
    {"name":"zwtUOo4hiq","marks":19},{"name":"CH79vONro","marks":50},{"name":"1GMVXjGz","marks":1},{"name":"LuI41fGFp","marks":9},
    {"name":"MYmS","marks":45},{"name":"ytSgX0XK","marks":51},{"name":"tvsZoKCJou","marks":8},{"name":"Rjeun","marks":34},
    {"name":"ywuIts5x","marks":62},{"name":"E50","marks":86},{"name":"yqf2O","marks":36},{"name":"H05N5","marks":96},
    {"name":"4","marks":26},{"name":"ciBzHmp9ee","marks":62},{"name":"et","marks":25},{"name":"P","marks":95},
    {"name":"CcjFO","marks":88},{"name":"Zn4Ce","marks":47},{"name":"VykjTh","marks":51},{"name":"f","marks":18},
    {"name":"6NEyE8A3r","marks":27},{"name":"l4","marks":61},{"name":"KgW","marks":2},{"name":"fIqo7qpD","marks":84},
    {"name":"vxnI6kYqET","marks":15},{"name":"o","marks":30},{"name":"Or9X7A","marks":43},{"name":"BHnDK","marks":22},
    {"name":"BOlGvHucx","marks":64},{"name":"yHLLXnaUqk","marks":9},{"name":"3BoDDSFX","marks":51},{"name":"n3dK90v92t","marks":79},
    {"name":"ob","marks":6},{"name":"d4idni05j4","marks":30},{"name":"rFI6A6","marks":22},{"name":"eUUdQ","marks":78},
    {"name":"BOzpVQ","marks":11},{"name":"kXI","marks":88},{"name":"njAl","marks":84},{"name":"GLtnvyl08","marks":79},
    {"name":"qB","marks":33},{"name":"MmirFCbJ8G","marks":32},{"name":"yPg13thFk","marks":13},{"name":"jm","marks":20},
    {"name":"V8MlC4u","marks":84},{"name":"TN","marks":70},{"name":"Onv8","marks":12},{"name":"GDJEY","marks":80},
    {"name":"n4b30tqbo7","marks":19},{"name":"UlxKHnaD","marks":99},{"name":"uNflbVKo4","marks":75},{"name":"d4mau3d6","marks":10},
    {"name":"q8g007n3E","marks":34},{"name":"doB","marks":22},{"name":"xWLTihL96f","marks":68},{"name":"j","marks":81},
    {"name":"GepOTGm","marks":92},{"name":"h5X","marks":66},{"name":"g04V8HeK","marks":53},{"name":"6JI9fs","marks":91},
    {"name":"PTRjAZ","marks":80},{"name":"9k2Jqz","marks":36},{"name":"yU00DhEaB","marks":83},{"name":"z1","marks":38},
    {"name":"p","marks":79},{"name":"N6jORax","marks":48},{"name":"eC6Eco6","marks":23},{"name":"S5f3baM0AY","marks":27},
    {"name":"csDCj","marks":93},{"name":"Xtx4pH9","marks":25},{"name":"OrfU","marks":18},{"name":"AvuHx5PdP","marks":67}
]

# Create dictionary for quick lookup
student_data = {item["name"]: item["marks"] for item in data}

@app.get("/api")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_data.get(name, None) for name in names]
    return {"marks": marks}
