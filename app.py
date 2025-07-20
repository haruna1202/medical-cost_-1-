
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("Model (99).pkl")

# Lưu lịch sử tạm trong RAM
history = []

@app.route('/')
def home():
    return render_template("form.html", result=None, history=history)

@app.route('/predict', methods=['POST'])
def predict():
    # Nhận dữ liệu từ form
    age = int(request.form['age'])
    sex = 1 if request.form['sex'] == 'male' else 0
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = 1 if request.form['smoker'] == 'yes' else 0
    region_map = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
    region = region_map[request.form['region']]

    # Dự đoán
    input_data = np.array([[age, sex, bmi, children, smoker, region]])
    predicted_cost = round(model.predict(input_data)[0], 2)

    # Thêm vào lịch sử
    history.append({
        "tuoi": age,
        "gioitinh": "Nam" if sex == 1 else "Nữ",
        "bmi": bmi,
        "con": children,
        "hutthuoc": "Có" if smoker == 1 else "Không",
        "khuvuc": request.form['region'],
        "ketqua": predicted_cost
    })

    return render_template("form.html", result=predicted_cost, history=history)

@app.route('/clear')
def clear_history():
    history.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
