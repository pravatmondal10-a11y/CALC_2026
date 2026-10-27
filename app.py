import streamlit as st
import math

# Page configuration
st.set_page_config(
    page_title="Python Calculator",
    page_icon="🧮",
    layout="centered"
)

# Application title
st.title("🧮 Python Calculator")
st.write("Select an operation and enter your numbers.")

# Select operator
operator = st.selectbox(
    "Select an operator:",
    ["+", "-", "*", "/"]
)

# Addition
if operator == "+":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="Example: 10,20,30"
    )

# Multiplication
elif operator == "*":
    values = st.text_input(
        "Enter values separated by commas:",
        placeholder="Example: 2,3,4"
    )

# Subtraction and division
else:
    num1 = st.number_input(
        "Please enter the first number:",
        value=0.0
    )

    num2 = st.number_input(
        "Please enter the second number:",
        value=0.0
    )

# Calculate button
if st.button("Calculate", type="primary"):

    try:
        # Addition
        if operator == "+":
            if not values.strip():
                st.warning("Please enter some numbers.")
            else:
                numbers = [
                    float(value.strip())
                    for value in values.split(",")
                ]

                if not all(math.isfinite(n) for n in numbers):
                    st.error("Please enter valid finite numbers.")
                else:
                    result = sum(numbers)
                    st.success(
                        f"Addition of all the given values: {result:g}"
                    )

        # Subtraction
        elif operator == "-":
            st.write(f"{num1:g} - {num2:g} = {num1 - num2:g}")
            st.write(f"{num2:g} - {num1:g} = {num2 - num1:g}")

        # Multiplication
        elif operator == "*":
            if not values.strip():
                st.warning("Please enter some numbers.")
            else:
                numbers = [
                    float(value.strip())
                    for value in values.split(",")
                ]

                if not all(math.isfinite(n) for n in numbers):
                    st.error("Please enter valid finite numbers.")
                else:
                    result = math.prod(numbers)
                    st.success(
                        f"Multiplication of all the given values: {result:g}"
                    )

        # Division
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
                st.success(f"{num1:g} / {num2:g} = {result:g}")
            else:
                st.error(
                    "You cannot divide by zero. Please try again."
                )

    except ValueError:
        st.error(
            "Invalid input! Please enter valid numbers separated by commas."
        )

# Footer
st.divider()
st.caption("Thank you for using the calculator!")
 