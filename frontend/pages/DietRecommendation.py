# pages/diet.py
import streamlit as st

def calculate_calories(age, height, weight, gender, activity_level, weight_loss_plan):
    result = f"Age: {age}, Height: {height} cm, Weight: {weight} kg, Gender: {gender}, Activity Level: {activity_level}, Weight Loss Plan: {weight_loss_plan}"
    return result

def show():
    st.markdown('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown('<style>div.Widget.row-widget.stSelectbox > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.markdown('<style>div.Widget.row-widget.stSlider > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.header('User Information:')
    with st.form("diet_input_form"):
        age = st.number_input('Age', 1, 100, 25)

        # Validation for age
        if age < 13 or age > 70:
            st.warning("Age should be between 13 and 70.")

        height = st.number_input('Height (cm)', 1, 300, 150)
        weight = st.number_input('Weight (kg)', 1, 200, 70)

        gender = st.radio('Gender', ['Male', 'Female'])

        activity = st.select_slider('Activity', options=['Little/no exercise', 'Light exercise', 'Moderate exercise (3-5 days/wk)', 'Very active (6-7 days/wk)', 
            'Extra active (very active & physical job)'])
        
        plans = ['Maintain weight', 'Lose weight', 'Gain weight']  # Add your actual weight loss plans
        option = st.selectbox('Choose your weight loss plan:', plans)

        # Assuming you have predefined weights for each plan, replace this line with your actual logic
        weights = {'Maintain weight': 0, 'Lose weight': -500, 'Gain weight': 500}
        weight_loss = weights.get(option, 0)

        number_of_meals = st.slider('Meals per day', min_value=3, max_value=5, step=1, value=3)

        generated_diet = st.form_submit_button("Generate Diet Plan")

    if generated_diet and age > 13 and age < 70:
        result = calculate_calories(age, height, weight, gender, activity, weight_loss)
        st.success(result)

if __name__ == "__main__":
    show()
