import streamlit as st
import pandas as pd
import math
from PIL import Image

# Initialize page state in session
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to navigate
def navigate_to(page_name):
    st.session_state.page = page_name

if st.session_state.page == 'home':
    st.title("A Modern Approach to Pendulum")
    st.subheader("What if...Galileo would have born in 21st century?")
    if st.button("Make a prediction"):
        navigate_to('page1')
    if st.button("Show result for small Angles"):
        navigate_to('page2')

elif st.session_state.page == 'page1':
    st.title("Make a prediction")
    length = st.number_input('Enter length in meters', key="length_input")
    mass = st.number_input('Enter mass in kilograms', key="mass_input")
    angle = st.number_input('Enter angle in degres (0°-90°)', key="angle_input")
    angle_rd = angle * math.pi / 180
    if (length < 0 or mass < 0 or angle < 0 or angle > 90):
        st.write('Wrong input please try again')
    if st.button('Calcola'):
        if angle > 20:
            df = pd.read_csv('coefficients.csv')
            intercept = df.at[0, 'Intercept']
            first_param = df.at[0, 'First Parameter(L)']
            second_param = df.at[0, 'Second Parameter (M)']
            third_param = df.at[0, 'Third Parameter (A)']
            prediction = 10 ** intercept * (length) ** first_param * (angle_rd) ** third_param / ((mass ** (-second_param)))
            th_prediction = 2 * math.pi * (length / 9.8) ** 0.5 * (1 + angle_rd ** 2 / 16)
            st.success(f'Model Prediction: {prediction:.2f} s')
            st.success(f'Theoretical Prediction: {th_prediction:.2f} s')
        else:
            df = pd.read_csv('coefficients_sa.csv')
            intercept = df.at[0, 'Intercept']
            slope = df.at[0, 'Slope']
            prediction = 10 ** intercept * (length) ** slope
            th_prediction = 2 * math.pi * (length / 9.8) ** 0.5
            st.success(f'Model Prediction for Small Angles: {prediction:.2f} s')
            st.success(f'Theoretical Prediction Small Angles: {th_prediction:.2f} s')

    if st.button("Back to Home"):
        navigate_to('home')

elif st.session_state.page == 'page2':
    st.title("Show result for small Angles")
    st.image("plots_by_angles.jpg", caption="Scatterplots and correlation matrix to data visualization", use_column_width=True)
    st.image("LR_small_angles.jpg", caption="Log Best fit", use_column_width=True)
    st.image("Comparison_plot_small_angles.jpg", caption="Interesting comparison between the Model and the Theory", use_column_width=True)

    with open('results_sa.txt', 'r') as file:
        info = file.readlines()

    st.write(info[0])
    st.write(info[1])
    st.write(info[2])

    if st.button("Back to Home"):
        navigate_to('home')

else:
    st.write("Select an option to proceed")

github_logo = Image.open('logo_github.png')
if st.button('GitHub'):
    st.markdown('[![GitHub]({})](https://github.com/tuo_username/tuo_repository)'.format(github_logo))





