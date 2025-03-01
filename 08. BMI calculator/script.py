import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0, format="%.0f")
height = st.number_input("Enter your height (m)", min_value=0.1, format="%.1f")

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        st.success(f"Your BMI is {bmi:.2f}, which is considered {category}.")
    else:
        st.error("Please enter valid weight and height values.")
