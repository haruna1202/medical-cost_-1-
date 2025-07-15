import streamlit as st
import pandas as pd
import joblib

# Load mô hình đã lưu (đúng tên file pkl)
model = joblib.load('Model (99).pkl')

# Tiêu đề ứng dụng
st.title("Dự đoán chi phí y tế cá nhân")
st.write("Nhập các thông tin bên dưới để dự đoán chi phí y tế:")

# Giao diện người dùng nhập dữ liệu
age = st.number_input("Tuổi", min_value=0, max_value=120, value=30)
sex = st.selectbox("Giới tính", ["male", "female"])
bmi = st.number_input("Chỉ số BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Số con", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Có hút thuốc?", ["yes", "no"])
region = st.selectbox("Khu vực", ["southeast", "southwest", "northeast", "northwest"])

# Gộp dữ liệu người dùng nhập thành dataframe
input_df = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'bmi': [bmi],
    'children': [children],
    'smoker': [smoker],
    'region': [region]
})

# Dự đoán khi người dùng bấm nút
if st.button("Dự đoán chi phí"):
    prediction = model.predict(input_df)
    st.success(f"Chi phí y tế ước tính: ${prediction[0]:,.2f}")
