# Dự đoán Chi Phí Y Tế Cá Nhân 🏥

Dự án này nhằm phân tích các yếu tố ảnh hưởng đến chi phí chăm sóc sức khỏe và dự đoán chi phí y tế cá nhân bằng các mô hình hồi quy. Ứng dụng sử dụng kỹ thuật học máy và được triển khai qua giao diện web với FastAPI.

---

## ✅ Mô hình cuối cùng: Hồi quy tuyến tính
Mô hình được sử dụng là **Linear Regression**, được huấn luyện trên bộ dữ liệu bảo hiểm y tế. Mô hình nhận các đặc trưng cá nhân và trả về kết quả ước tính chi phí y tế.

- Mô hình: `LinearRegression()`
- Triển khai: FastAPI + Biểu mẫu HTML
- Giao diện: Form web nhập thông tin (tuổi, giới tính, BMI, hút thuốc, số con, khu vực)

---

## 🔍 Phát hiện & phân tích chính
1. **Hút thuốc** là yếu tố ảnh hưởng mạnh nhất đến chi phí y tế.
2. Người có **BMI cao (trên 30)** thường có chi phí điều trị cao hơn.
3. **Tuổi** càng lớn thì chi phí y tế càng tăng.
4. **Số con phụ thuộc** có ảnh hưởng nhẹ đến chi phí.
5. **Giới tính và khu vực** gần như không ảnh hưởng nhiều đến chi phí.

---

## 💡 Dữ liệu sử dụng
Bộ dữ liệu dùng để huấn luyện mô hình dự đoán chi phí y tế dựa trên đặc điểm cá nhân.

- Đặc trưng đầu vào: `age`, `sex`, `bmi`, `children`, `smoker`, `region`
- Biến mục tiêu: `charges`

**Nguồn dữ liệu:** [Kaggle - Medical Cost Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance/data)

---

## ⚙️ Công cụ & thư viện sử dụng
**Ngôn ngữ lập trình:** Python  
**Xử lý dữ liệu:** pandas, numpy  
**Trực quan hóa:** matplotlib, seaborn  
**Học máy:** scikit-learn (LinearRegression)  
**Triển khai web:** FastAPI + Jinja2 Templates  
**Lưu mô hình:** joblib  
**Môi trường phát triển:** Google Colab (huấn luyện mô hình), VS Code (triển khai FastAPI)

---

## 🚀 Cách chạy ứng dụng

```bash
# Cài thư viện
pip install -r requirements.txt

# Chạy ứng dụng FastAPI
uvicorn main:app --reload
```

Mở trình duyệt tại:
```
http://127.0.0.1:5000/```

---

## 📁 Cấu trúc thư mục dự án
```
medical-cost/
├── main.py                # Backend FastAPI
├── Model (99).pkl         # Mô hình đã huấn luyện
├── requirements.txt       # Thư viện cần cài
└── templates/
    └── form.html          # Giao diện HTML nhập liệu
```

---

## ✨ Giao diện minh họa
Giao diện người dùng thân thiện cho phép nhập dữ liệu và nhận dự đoán chi phí y tế theo thời gian thực.

---

Tạo bởi ❤️ sử dụng FastAPI và Hồi quy tuyến tính.
