import streamlit as st

st.title("Frogglicker Rocket Tools")
"These pages contains several simple, and commonly used tools for model rocketry"
st.divider()

tab1, tab2, tab3, tab4 = st.tabs(["Conversions","Thrust to Weight","Common Tubes","Links"])



with tab1:
    st.subheader("Conversion Calculators")
    st.divider()
    col1, col2, col3, col4, = st.columns([50,15,50,15])
    with col1:
        # MM to IN
        st.subheader("Millimeters to Inches")
        col1, col2 = st.columns([2,2])
        with col1:
            mm = st.number_input(label="Enter millimeters", step=0.1, min_value=0.0, value="min", max_value=100000.0)
        with col2:
            if mm is not None:
                inches = round(float(mm)/25.4,4)
                "Result"
                st.code(inches, language="python")

        #IN to MM
        st.subheader("Inches to Millimeters")
        col1, col2 = st.columns([2,2])
        with col1:
            inches2 = st.number_input("Enter inches:", step=0.125, min_value=0.0, value="min", max_value=100000.0)
        with col2:
            if inches2 is not None:
                mm2 = round(float(inches2)*25.4,4)
                "Result"
                st.code(mm2, language="python")

        #Meters to Feet
        st.subheader("Meters to Feet")
        col1, col2 = st.columns([2, 2])
        with col1:
            meters1 = st.number_input("Enter meters :", step=1.0, min_value=0.0, value="min", max_value=100000.0)
        with col2:
            if meters1 is not None:
                feet1 = round(float(meters1)* 3.28084,4)
                "Result"
                st.code(feet1, language="python")

        #Feet to Meters
        st.subheader("Feet to Meters")
        col1, col2 = st.columns([2,2])
        with col1:
            feet2 = st.number_input("Enter feet :", step=1.0, min_value=0.0, value="min", max_value=100000.0)
        with col2:
            if feet2 is not None:
               meters2 = round(float(feet2)/3.28084,4)
               "Result"
               st.code(meters2, language="python")
    with col3:
        # Scale to Perc
        st.subheader("Scale to Percentage")
        col1, col2 = st.columns([2, 2])
        with col1:
            orig_val = st.number_input("Current Value :")
            perc     = st.number_input("Percentage :", step=0.0, min_value=0.0, value="min", max_value=999.9)
        with col2:
            if orig_val is not None and perc is not None:
                scale = round(orig_val * perc / 100, 4)
                "Scaled Result"
                st.code(scale, language="python")

        # Scale Object
        st.subheader("Percent from Values")
        col1, col2 = st.columns([2, 2])
        with col1:
            value_1 = st.number_input("Enter original length :", step=1.0, min_value=0.0, value="min", max_value=100000.0)
            value_2 = st.number_input("Enter scaled length :", step=1.0, min_value=0.0, value="min", max_value=100000.0)
        with col2:
            if value_1 is not None and value_2 is not None and value_2 > 0.0:
                percent = round(value_2/value_1*100, 4)
                "Percent Result"
                st.code(percent, language="python")
with tab2:
    st.subheader("Thrust to Weight Calculator")
    # measurement_system = st.radio("Select the unit type",
    #                               ["Metric", "Imperial"], index="Metric",)

    genre = st.radio(
        "Select the unit type",
        ["Metric", "Imperial"],
        index=None,
    )

    st.write("You selected:", genre)

with tab3:
    st.subheader("Tube Sizes")

with tab4:
    st.subheader("links")
