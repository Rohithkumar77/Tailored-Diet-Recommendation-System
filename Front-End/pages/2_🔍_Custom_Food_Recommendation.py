# Assuming you have a Recommendation class or function
class Recommendation:
    def __init__(self, nutritions_values_list, nb_recommendations, ingredient_txt):
        self.nutritions_values_list = nutritions_values_list
        self.nb_recommendations = nb_recommendations
        self.ingredient_txt = ingredient_txt

    def generate(self):
        # Implement the logic to generate recommendations based on user input
        # You can use the nutritional values and optional ingredients here
        # Replace the following line with your actual implementation
        recommendations = ["Recommendation1", "Recommendation2", "Recommendation3"]
        return recommendations

# Rest of your Streamlit code
import streamlit as st

with st.form("input_form"):
    st.header('Nutritional values:')
    Calories = st.slider('Calories', 0, 2000, 500)
    FatContent = st.slider('FatContent', 0, 100, 50)
    SaturatedFatContent = st.slider('SaturatedFatContent', 0, 13, 0)
    CholesterolContent = st.slider('CholesterolContent', 0, 300, 0)
    SodiumContent = st.slider('SodiumContent', 0, 2300, 400)
    CarbohydrateContent = st.slider('CarbohydrateContent', 0, 325, 100)
    FiberContent = st.slider('FiberContent', 0, 50, 10)
    SugarContent = st.slider('SugarContent', 0, 40, 10)
    ProteinContent = st.slider('ProteinContent', 0, 40, 10)
    nutritions_values_list = [Calories, FatContent, SaturatedFatContent, CholesterolContent, SodiumContent, CarbohydrateContent, FiberContent, SugarContent, ProteinContent]

    st.header('Recommendation options (OPTIONAL):')
    nb_recommendations = st.slider('Number of recommendations', 5, 20, step=5)
    ingredient_txt = st.text_input('Specify ingredients to include in the recommendations separated by ";" :', placeholder='Ingredient1;Ingredient2;...')
    st.caption('Example: Milk;eggs;butter;chicken...')

    generated = st.form_submit_button("Generate")

if generated:
    with st.spinner('Generating recommendations...'): 
        recommendation = Recommendation(nutritions_values_list, nb_recommendations, ingredient_txt)
        recommendations = recommendation.generate()
        st.session_state.recommendations = recommendations
    st.session_state.generated = True
