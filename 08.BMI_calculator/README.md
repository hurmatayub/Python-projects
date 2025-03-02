# BMI Calculator

This is a simple **BMI (Body Mass Index) Calculator** web application built using **Streamlit**.

## Live Demo

[Click here to try the BMI Calculator](https://bmi-calculator-by-hurmat-ayub.streamlit.app/)

## Features

- Input weight in **kilograms (kg)**
- Input height in **meters (m)**
- Calculates **BMI** using the formula:
  ```python
  BMI = weight / (height ** 2)
  ```
- Categorizes BMI into:
  - **Underweight**: BMI < 18.5
  - **Normal weight**: 18.5 ≤ BMI < 24.9
  - **Overweight**: 25 ≤ BMI < 29.9
  - **Obese**: BMI ≥ 30
- Displays BMI result along with its category.

## Technologies Used

- **Python**
- **Streamlit**

## How It Works

1. Users enter their weight (in kg) and height (in meters).
2. Clicking the **Calculate BMI** button computes their BMI.
3. The app displays the **BMI value** and the corresponding **BMI category**.
4. If invalid values are entered, an error message is shown.

## Example

**Input:**

- Weight: **70 kg**
- Height: **1.75 m**

**Output:**

> Your BMI is **22.86**, which is considered **Normal weight**.
>
> ## Author

**Hurmat Muhammad Ayub**

