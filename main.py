from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")

model = joblib.load("Model (99).pkl")

@app.get("/", response_class=HTMLResponse)
async def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request, "result": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request,
                  age: int = Form(...),
                  sex: str = Form(...),
                  bmi: float = Form(...),
                  children: int = Form(...),    
                  smoker: str = Form(...),
                  region: str = Form(...)):

    # Mã hóa các biến phân loại
    sex = 1 if sex == "male" else 0
    smoker = 1 if smoker == "yes" else 0
    region_map = {
        "northeast": 0,
        "northwest": 1,
        "southeast": 2,
        "southwest": 3
    }
    region = region_map.get(region.lower(), 0)

    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "bmi": [bmi],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    prediction = model.predict(input_df)[0]
    return templates.TemplateResponse("form.html", {
        "request": request,
        "result": f"${prediction:,.2f}"
    })
