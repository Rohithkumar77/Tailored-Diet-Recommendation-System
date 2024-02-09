import streamlit as st

def calculate_calories(age, height, weight, gender, activity_level, weight_loss_plan):
    result = f"Age: {age}, Height: {height} cm, Weight: {weight} kg, Gender: {gender}, Activity Level: {activity_level}, Weight Loss Plan: {weight_loss_plan}"
    return result

st.title('Automatic Diet Recommendation')

with st.form("input_form"):
    age = st.number_input('Age', 1, 100, 25)
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

    generated = st.form_submit_button("Generate")

if generated:
    result = calculate_calories(age, height, weight, gender, activity, weight_loss)
    st.success(result)
