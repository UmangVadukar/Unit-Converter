import streamlit as st

# Unit converter function
def unit_converter():
    st.title("Unit Converter")
    st.write("===============")

    unit_change = {
        1: "Length",
        2: "Mass",
        3: "Temperature",
        4: "Time",
        5: "Speed",
        6: "Energy",
        7: "Pressure"
    }

    # Select conversion type
    change = st.selectbox("Select type of conversion", list(unit_change.values()))

    if change == "Length":
        length_dict = {
            1: "Centimeter to Meter",
            2: "Meter to Centimeter",
            3: "Centimeter to Inch",
            4: "Inch to Centimeter",
            5: "Centimeter to Kilometer",
            6: "Kilometer to Centimeter",
            7: "Centimeter to Foot",
            8: "Foot to Centimeter",
            9: "Kilometer to Mile",
            10: "Mile to Kilometer"
        }
        length_convert = st.selectbox("Choose conversion", list(length_dict.values()))
        length_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if length_convert == "Centimeter to Meter":
                st.write(f"{length_value} cm is equal to {length_value / 100} m.")
            elif length_convert == "Meter to Centimeter":
                st.write(f"{length_value} m is equal to {length_value * 100} cm.")
            elif length_convert == "Centimeter to Inch":
                st.write(f"{length_value} cm is equal to {length_value / 2.54} inch.")
            elif length_convert == "Inch to Centimeter":
                st.write(f"{length_value} inch is equal to {length_value * 2.54} cm.")
            elif length_convert == "Centimeter to Kilometer":
                st.write(f"{length_value} cm is equal to {length_value / 100000} km.")
            elif length_convert == "Kilometer to Centimeter":
                st.write(f"{length_value} km is equal to {length_value * 100000} cm.")
            elif length_convert == "Centimeter to Foot":
                st.write(f"{length_value} cm is equal to {length_value / 30.48} feet.")
            elif length_convert == "Foot to Centimeter":
                st.write(f"{length_value} feet is equal to {length_value * 30.48} cm.")
            elif length_convert == "Kilometer to Mile":
                st.write(f"{length_value} km is equal to {length_value / 1.609} miles.")
            elif length_convert == "Mile to Kilometer":
                st.write(f"{length_value} miles is equal to {length_value * 1.609} km.")
    
    elif change == "Mass":
        mass_dict = {
            1: "Gram to Kilogram",
            2: "Kilogram to Gram",
            3: "Kilogram to Tonne",
            4: "Tonne to Kilogram",
            5: "Milligram to Kilogram",
            6: "Kilogram to Milligram",
            7: "Milligram to Gram",
            8: "Gram to Milligram",
            9: "Kilogram to Pound",
            10: "Pound to Kilogram",
            11: "Micrograms to Gram",
            12: "Micrograms to Kilogram"
        }
        mass_convert = st.selectbox("Choose conversion", list(mass_dict.values()))
        mass_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if mass_convert == "Gram to Kilogram":
                st.write(f"{mass_value} g is equal to {mass_value / 1000} Kg")
            elif mass_convert == "Kilogram to Gram":
                st.write(f"{mass_value} Kg is equal to {mass_value * 1000} g")
            elif mass_convert == "Kilogram to Tonne":
                st.write(f"{mass_value} kg is equal to {mass_value / 1000} T")
            elif mass_convert == "Tonne to Kilogram":
                st.write(f"{mass_value} T is equal to {mass_value * 1000} kg")
            elif mass_convert == "Milligram to Kilogram":
                st.write(f"{mass_value} mg is equal to {mass_value / 1000000} kg")
            elif mass_convert == "Kilogram to Milligram":
                st.write(f"{mass_value} Kg is equal to {mass_value * 1000000} mg")
            elif mass_convert == "Milligram to Gram":
                st.write(f"{mass_value} mg is equal to {mass_value / 1000} g")
            elif mass_convert == "Gram to Milligram":
                st.write(f"{mass_value} g is equal to {mass_value * 1000} mg")
            elif mass_convert == "Kilogram to Pound":
                st.write(f"{mass_value} Kg is equal to {mass_value * 2.20462} lb")
            elif mass_convert == "Pound to Kilogram":
                st.write(f"{mass_value} lb is equal to {mass_value / 2.20462} kg")
            elif mass_convert == "Micrograms to Gram":
                st.write(f"{mass_value} μg is equal to {mass_value / 1e+6} g")
            elif mass_convert == "Micrograms to Kilogram":
                st.write(f"{mass_value} μg is equal to {mass_value / 1e+9} kg")
    
    elif change == "Temperature":
        temp_dict = {
            1: "Celsius to Fahrenheit",
            2: "Celsius to Kelvin",
            3: "Fahrenheit to Celsius",
            4: "Fahrenheit to Kelvin",
            5: "Kelvin to Celsius",
            6: "Kelvin to Fahrenheit"
        }
        temp_convert = st.selectbox("Choose conversion", list(temp_dict.values()))
        temp_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if temp_convert == "Celsius to Fahrenheit":
                st.write(f"{temp_value} C is equal to {(temp_value * 1.8) + 32} F")
            elif temp_convert == "Celsius to Kelvin":
                st.write(f"{temp_value} C is equal to {temp_value + 273.15} K")
            elif temp_convert == "Fahrenheit to Celsius":
                st.write(f"{temp_value} F is equal to {(temp_value - 32) * 1.8} C")
            elif temp_convert == "Fahrenheit to Kelvin":
                st.write(f"{temp_value} F is equal to {(temp_value - 32) * 1.8 + 273.15} K")
            elif temp_convert == "Kelvin to Celsius":
                st.write(f"{temp_value} K is equal to {temp_value - 273.15} C")
            elif temp_convert == "Kelvin to Fahrenheit":
                st.write(f"{temp_value} K is equal to {(temp_value - 273.15) * 1.8 + 32} F")
    
    elif change == "Time":
        time_dict = {
            1: "Second to Minute",
            2: "Minute to Second",
            3: "Second to Hour",
            4: "Minute to Hour",
            5: "Hour to Minute",
            6: "Day to Hour",
            7: "Hour to Day"
        }
        time_convert = st.selectbox("Choose conversion", list(time_dict.values()))
        time_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if time_convert == "Second to Minute":
                st.write(f"{time_value} S is equal to {time_value / 60} M")
            elif time_convert == "Minute to Second":
                st.write(f"{time_value} M is equal to {time_value * 60} S")
            elif time_convert == "Second to Hour":
                st.write(f"{time_value} S is equal to {time_value / 3600} H")
            elif time_convert == "Minute to Hour":
                st.write(f"{time_value} M is equal to {time_value / 60} H")
            elif time_convert == "Hour to Minute":
                st.write(f"{time_value} H is equal to {time_value * 60} M")
            elif time_convert == "Day to Hour":
                st.write(f"{time_value} day is equal to {time_value * 24} H")
            elif time_convert == "Hour to Day":
                st.write(f"{time_value} H is equal to {time_value / 24} day")
    
    elif change == "Speed":
        speed_dict = {
            1: "Mile per hour to Kilometer per hour",
            2: "Kilometer per hour to Mile per hour",
            3: "Mile per hour to Meter per Second",
            4: "Meter per Second to Mile per hour",
            5: "Kilometer per hour to Meter per Second",
            6: "Meter per Second to Kilometer per hour"
        }
        speed_convert = st.selectbox("Choose conversion", list(speed_dict.values()))
        speed_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if speed_convert == "Mile per hour to Kilometer per hour":
                st.write(f"{speed_value} Ml/h is equal to {speed_value * 1.609} Km/h")
            elif speed_convert == "Kilometer per hour to Mile per hour":
                st.write(f"{speed_value} Km/h is equal to {speed_value / 1.609} Ml/h")
            elif speed_convert == "Mile per hour to Meter per Second":
                st.write(f"{speed_value} Ml/h is equal to {speed_value / 2.237} m/s")
            elif speed_convert == "Meter per Second to Mile per hour":
                st.write(f"{speed_value} m/s is equal to {speed_value * 2.237} Ml/h")
            elif speed_convert == "Kilometer per hour to Meter per Second":
                st.write(f"{speed_value} Km/h is equal to {speed_value / 3.6} m/s")
            elif speed_convert == "Meter per Second to Kilometer per hour":
                st.write(f"{speed_value} m/s is equal to {speed_value * 3.6} Km/h")

    elif change == "Energy":
        energy_dict = {
            1: "Joule to Kilojoule",
            2: "Kilojoule to Joule",
            3: "Joule to Kilocalorie",
            4: "Kilocalorie to Joule",
            5: "Kilojoule to Kilocalorie",
            6: "Kilocalorie to Kilojoule"
        }
        energy_convert = st.selectbox("Choose conversion", list(energy_dict.values()))
        energy_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if energy_convert == "Joule to Kilojoule":
                st.write(f"{energy_value} J is equal to {energy_value / 1000} Kj")
            elif energy_convert == "Kilojoule to Joule":
                st.write(f"{energy_value} Kj is equal to {energy_value * 1000} J")
            elif energy_convert == "Joule to Kilocalorie":
                st.write(f"{energy_value} J is equal to {energy_value / 4184} kcal")
            elif energy_convert == "Kilocalorie to Joule":
                st.write(f"{energy_value} kcal is equal to {energy_value * 4184} J")
            elif energy_convert == "Kilojoule to Kilocalorie":
                st.write(f"{energy_value} Kj is equal to {energy_value * 239} kcal")
            elif energy_convert == "Kilocalorie to Kilojoule":
                st.write(f"{energy_value} kcal is equal to {energy_value / 239} Kj")

    elif change == "Pressure":
        pressure_dict = {
            1: "Bar to Pascal",
            2: "Bar to Standard atmosphere",
            3: "Pascal to Bar",
            4: "Pascal to Standard atmosphere",
            5: "Standard atmosphere to Pascal",
            6: "Standard atmosphere to Bar"
        }
        pressure_convert = st.selectbox("Choose conversion", list(pressure_dict.values()))
        pressure_value = st.number_input("Enter a number to convert", min_value=0.0)

        # Calculate conversion and display result when button is clicked
        if st.button('Calculate'):
            if pressure_convert == "Bar to Pascal":
                st.write(f"{pressure_value} Bar is equal to {pressure_value * 100000} Pascal")
            elif pressure_convert == "Bar to Standard atmosphere":
                st.write(f"{pressure_value} Bar is equal to {pressure_value / 1.013} atm")
            elif pressure_convert == "Pascal to Bar":
                st.write(f"{pressure_value} Pascal is equal to {pressure_value / 100000} Bar")
            elif pressure_convert == "Pascal to Standard atmosphere":
                st.write(f"{pressure_value} Pascal is equal to {pressure_value / 101325} atm")
            elif pressure_convert == "Standard atmosphere to Pascal":
                st.write(f"{pressure_value} atm is equal to {pressure_value * 101325} Pascal")
            elif pressure_convert == "Standard atmosphere to Bar":
                st.write(f"{pressure_value} atm is equal to {pressure_value * 1.013} Bar")

if __name__ == "__main__":
    unit_converter()
