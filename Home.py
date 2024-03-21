import streamlit as st

st.set_page_config(page_title="Home", page_icon="🥗", layout="wide")


# Define the custom CSS for the background image


#background-color: blue; # background-image: url("https://github.com/Rohithkumar77/Tailored-Diet-Recommendation-System/blob/main/assets/bg.jpeg");
# Streamlit app content


link = "https://github.com/Rohithkumar77/Tailored-Diet-Recommendation-System/raw/main/assets/Tlogo.png"
markdown_content = f"""
    <div style='display: flex; align-items: center;'>
        <img src='{link}' style='width: 40px; height: 40px; border-radius: 50px;'/> 
        <span style='color: black; font-size: 48px; font-weight: bold; margin-top: -5px;'>Welcome to Tailored Diet Recommendation System</span>
    </div>
    <style>
        @media only screen and (max-width: 600px) {{
            span {{
                font-size: 24px !important;
            }}
        }}
    </style>
"""
st.markdown(markdown_content, unsafe_allow_html=True)

def main():
    st.sidebar.markdown(f"<span style='color: black;font-size: 36px;font-weight: bold;'>Diet Recommendation</span>", unsafe_allow_html=True)
    st.sidebar.info("Welcome to our project diet recommendation. Here you can analyze the nutritional value of food")
    st.sidebar.subheader("Check out our [Github Repository](https://)")

    st.subheader("Your personalized diet and nutrition assistant.")

    # About section
    with st.container():
        st.write("Our diet recommendation system is designed to help you make healthier food choices and achieve your nutrition goals. With our system, you can:")
        st.write("- Generate personalized meal plans based on your dietary preferences and nutritional needs")
        st.write("- Get detailed nutrition information of foods")

    # Features section
    with st.container():
        st.write("Our system offers the following features:")
        col1, col2 = st.columns(2)
        with col1:
            st.image("./assets/diet.jpeg", width=350) 
            st.write("- Personalized meal plans")

        with col2:
            st.image("./assets/custom.jpeg", width=350)
            st.write("- Recipe recommendations")

    # How It Works section
    with st.container():
        st.header("How It Works")
        st.write("Our system uses advanced algorithms to analyze your dietary preferences, nutritional goals, and lifestyle. Based on this analysis, it generates personalized meal plans and recipe recommendations that align with your goals. Here's a simple step-by-step process:")
        steps = [
            "1. Enter your personal information and dietary preferences.",
            "2. Select your nutritional goals and any specific dietary restrictions.",
            "3. The system generates a personalized meal plan and recipe recommendations.",
            "4. Access detailed nutritional information for each recommended recipe."
            ]
        for step in steps:
            st.write(step)

    # Benefits section
    with st.container():
        st.header("Benefits")
        st.write("By using our diet recommendation system, you can enjoy several benefits:")
        benefits = [
            "- Personalized meal plans tailored to your needs and preferences.",
            "- Access to a wide range of recipes that meet your nutritional goals.",
            "- Detailed nutritional information for each recipe to help you make informed dietary choices.",
            ]
        for benefit in benefits:
            st.write(benefit)

if __name__ == "__main__":
    main()
