import streamlit as st

# Title and "Made by" line
st.title("All-in-One Converter 🔄")

# Unit Conversion Categories with Icons
st.markdown("### Select Conversion Type:")
conversion_type = st.selectbox(
    "",
    ["Temperature 🌡️", "Length 📏", "Volume 💧", "Mass ⚖️", "Speed 🏃", "Time ⏱️", "Frequency 📶"]
)

# Define available units for each category
units_dict = {
    "Length 📏": ["m", "km", "cm", "mile", "yard", "inch"],
    "Mass ⚖️": ["g", "kg", "lb", "oz", "ton"],
    "Volume 💧": ["l", "ml", "gal", "m³", "qt"],
    "Speed 🏃": ["m/s", "km/h", "mph", "ft/s"],
    "Time ⏱️": ["s", "min", "h", "day", "week"],
    "Temperature 🌡️": ["celsius", "fahrenheit", "kelvin"],
    "Frequency 📶": ["hertz", "kilohertz", "megahertz"]
}

# Get units based on selected conversion type
selected_units = units_dict[conversion_type]

# Conversion inputs
value = st.number_input("Enter Value", value=1.0, format="%.2f")
from_unit = st.selectbox("From Unit", selected_units)
to_unit = st.selectbox("To Unit", selected_units)

# Function for converting Temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "fahrenheit" and to_unit == "kelvin":
        return ((value - 32) * 5/9) + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    elif from_unit == "kelvin" and to_unit == "fahrenheit":
        return ((value - 273.15) * 9/5) + 32
    else:
        return value

# When user clicks the Convert button
if st.button("Convert"):
    try:
        if conversion_type == "Temperature 🌡️":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            # Conversion factors for other units
            conversion_factors = {
                "Length 📏": {
                    "m": 1,
                    "km": 1000,
                    "cm": 0.01,
                    "mile": 1609.34,
                    "yard": 0.9144,
                    "inch": 0.0254
                },
                "Mass ⚖️": {
                    "g": 1,
                    "kg": 1000,
                    "lb": 453.592,
                    "oz": 28.3495,
                    "ton": 1_000_000
                },
                "Volume 💧": {
                    "l": 1,
                    "ml": 0.001,
                    "gal": 3.78541,
                    "m³": 1000,
                    "qt": 0.946353
                },
                "Speed 🏃": {
                    "m/s": 1,
                    "km/h": 0.277778,
                    "mph": 0.44704,
                    "ft/s": 0.3048
                },
                "Time ⏱️": {
                    "s": 1,
                    "min": 60,
                    "h": 3600,
                    "day": 86400,
                    "week": 604800
                },
                "Frequency 📶": {
                    "hertz": 1,
                    "kilohertz": 1000,
                    "megahertz": 1_000_000
                }
            }

            factors = conversion_factors[conversion_type]
            result = value * (factors[from_unit] / factors[to_unit])

        st.success(f"{value} {from_unit} is equal to **{result:.4f} {to_unit}**")

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("---")
st.markdown("Made by Qurratulain Haider")
