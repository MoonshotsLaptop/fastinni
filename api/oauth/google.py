from fastapi.routing import APIRouter

app = APIRouter(prefix="/google")

@app.route("/")
def index():
    pass

@app.route("/callback")
def callback():
    pass