import streamlit as st

col1, col2 = st.columns([2,10])
st.title("Frogglicker's Rocket Tools")
"These pages contains several simple, and commonly used tools for model rocketry"
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Conversions","Thrust to Weight","Common Tubes","Links", "Videos"])

with col1:
    st.image("froggy3_xsmall.png")

with col2:
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
        unit_type = st.radio(
            "Select the unit type:",
            ["Metric","Imperial"],
            index=None)

        if unit_type == "Metric":
            units={"force": "Newtons","mass": "Grams"}
        elif unit_type == "Imperial":
            units={"force": "lbF","mass": "ounces"}

        if unit_type is not None:
            thrust = st.number_input(key="thrust", label=f"Enter _Thrust_ in {units.get('force')}:", step=0.1, min_value=0.0)
            mass   = st.number_input (key="mass", label=f"Enter the _Mass_ in {units.get('mass')}:", step=0.01,min_value=0.0)

            if (thrust and thrust != 0) and (mass and mass !=0):
                if unit_type == "Metric":
                    gravity         = 9.81
                    mass_convertion = 1000  #gm_to_kilo
                else:
                    gravity         = 32.174
                    mass_convertion = 16 #oz to pounds
                weight = (mass / mass_convertion) * gravity
                ratio  = str(round(thrust / weight, 2))
                st.divider()
                
                st.metric(label="Thrust to Weight Ratio", value=f"{ratio} : 1")

    with tab3:
        st.subheader("Tube Sizes")

    with tab4:
        st.subheader("links")

    with tab5:
        vids = [
            {"title": "LOC Goblin 4 inch - Spooktacular Rocket Maiden Launch", "url": "https://youtu.be/37W8nDePSp0"},
            {"title": "Mega Red Max Rocket - Maiden Launch Highlights (Mega Der Red Max)", "url":"https://youtu.be/-IoUA4amfvw"}
        ]
        for vid in vids:
            with st.popover(label=vid.get("title")):
                st.video(vid.get("url"), format="video/mp4")
