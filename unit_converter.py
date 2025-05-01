import streamlit as st

# My app title

st.title("🌎Unit Converter App")
st.markdown("### Convert Lenght, Width and Time instantly")
st.write(" Welcome! select a category, enter a value and get the coverted results.")

# user input for category

category = st.selectbox("Choose a category", ["Lenght", "Weight", "Time"])

def convert_units(category,value,unit):
    if category == "Lenght":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to Pounds":
            return value *  2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
        
    # return 0
        
if category == "Lenght":
    unit = st.selectbox("📏Select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])

elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversation", ["kilograms to Pounds", "Pounds to Kilograms"])

elif category == "Time":
    unit = st.selectbox("⏲ Select Conversation", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")
