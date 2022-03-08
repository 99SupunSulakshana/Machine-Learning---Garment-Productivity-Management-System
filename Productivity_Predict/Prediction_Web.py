import numpy as np
import pickle
import streamlit as st
import requests
from streamlit_lottie import st_lottie


# loading our trained model
load_model = pickle.load(open('E:/Computational Assignment/productivity.sav', 'rb'))


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_code = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_o5dfcnmb.json")
lottie_code1 = load_lottieurl("https://assets5.lottiefiles.com/datafiles/ycpENSAUiWGIYZC/data.json")
lottie_code2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_w98qte06.json")
lottie_code3 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_mn0yeqfs.json")
# Create prediction function
def productivity_predict(input_data):

    # changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # standardize the input data
    # std_data = scaler.transform(input_data_reshaped)

    prediction = load_model.predict(input_data_reshaped)
    print('Your Productivity =', prediction)

    return prediction

def main():

    # Web app title


    menu = ["Prediction", "Home"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Prediction":

        st.container()
        st.title('EMPLOYEE PRODUCTIVITY IN ABC GARMENT')

        st.image("Assests//img1.jpg")
        with st.container():
            st.write("---")
            st.header("Additional Information Before Your Prediction")
            st.write(
                """
                - Please add numerical values for your prediction.
                """
            )
            left_column, center_column, right_column = st.columns(3)
            with left_column:
                st.write("##")
                st.subheader("Quarters Details")
                st.write(
                    """
                    - Quarter1 = 1
                    - Quarter2 = 2
                    - Quarter3 = 3
                    - Quarter4 = 4
                    - Quarter5 = 5
                    
                    """
                )
            with center_column:
                st.write("##")
                st.subheader("Department Details")
                st.write(
                    """
                    - Sweing = 1
                    - Finishing = 2
                    
                    """
                )
            with right_column:
                st.write("##")
                st.subheader("Week Day Details")
                st.write(
                    """
                    - Sunday = 1
                    - Monday = 2
                    - Tuesday = 3
                    - Wednesday = 4
                    - Thursday = 5
                    - Saturday = 6
                    """
                )



        # get the user input

        quarters = [1,2,3,4,5]
        departments = [1,2]
        day = [1,2,3,4,5,6]

        st.write("---")
        quarter = st.selectbox('Enter the Quarter Number (required)', quarters)
        department = st.selectbox('Enter the Department of the garment', departments)
        day = st.selectbox('Enter the day', day)
        team = st.slider('Enter the No of team', min_value=0, max_value=100)
        targeted_productivity = st.number_input('Enter the target productivity')
        smv = st.text_input('Enter the Standard Minute Value')
        wip = st.slider('Enter the Work in progress/ Unfinished items for products', min_value=0, max_value=5000)
        over_time = st.slider('Enter the amount of overtime', min_value=0, max_value=50000)
        incentive = st.slider('Enter the amount of financial incentive', min_value=0, max_value=250)
        idle_time = st.slider('The amount of time when the production was interrupted due to several reasons', min_value=0, max_value=250)
        idle_men = st.slider('The number of workers who were idle due to production interruption', min_value=0, max_value=250)
        no_of_style_change = st.slider('Number of changes in the style of a particular product', min_value=0, max_value=250)
        no_of_workers = st.slider('No of workers', min_value=0, max_value=500)

        actual_productivity = ''

        st_lottie(lottie_code1, height=300, key="coding1")

        # Button for Prediction
        if st.button('Productivity Result'):
            actual_productivity = productivity_predict([quarter, department, day, team,
                                                        targeted_productivity, smv, wip,
                                                        over_time, incentive, idle_time, idle_men,
                                                        no_of_style_change, no_of_workers])

        st.write('---')
        st.success(actual_productivity)
    # Home Page
    else:
        # Header Section
        left_column, right_column = st.columns(2)
        with left_column:
            st.subheader("Hii HR Management")
            st.write("---")
        with right_column:
            st_lottie(lottie_code1, height=300, key="coding1")


        st.title('WELCOME TO ABC GARMENT SYSTEM')
        st.write("ABC Garment Clothing provides bespoke apparel supply-chain solutions based on sustainabiliy and ethical manufacturing.")

        # --- what I do for ----
        # ---- WHAT I DO ----
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("What I do")
                st.write("##")
                st.write(
                    """
                    Primarily, HR Management should take the necessary steps to increase the productivity of the organization. We appreciate you as the main arm of the organization.
                    - Make sure to identify the weaknesses and strengths of all the departments using this system on a daily basis.
                    - Maintain corporate target productivity on a daily basis
                    - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
                    - are working with Excel and found themselves thinking - "there has to be a better way."
                    If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                    """
                )
                #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
            with right_column:
                st_lottie(lottie_code, height=500, key="coding")
        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st_lottie(lottie_code2, height=300, key="coding2")
            with right_column:
                st.header("The nature of the data you have to control")
                st.subheader("Attribute Information:")
                st.write("##")
                st.write(
                    """
                    - 01 date : Date in MM-DD-YYYY
                    - 02 day : Day of the Week
                    - 03 quarter : A portion of the month. A month was divided into four quarters
                    - 04 department : Associated department with the instance
                    - 05 teamno : Associated team number with the instance 
                    - 06 noofworkers : Number of workers in each team 
                    - 07 noofstylechange : Number of changes in the style of a particular product
                    - 08 targetedproductivity : Targeted productivity set by the Authority for each team for each day.
                    - 09 smv : Standard Minute Value, it is the allocated time for a task
                    - 10 wip : Work in progress. Includes the number of unfinished items for products
                    - 11 overtime : Represents the amount of overtime by each team in minutes
                    - 12 incentive : Represents the amount of financial incentive (in BDT) that enables or motivates a particular course of action.
                    - 13 idletime : The amount of time when the production was interrupted due to several reasons
                    - 14 idlemen : The number of workers who were idle due to production interruption
                    - 15 actual_productivity : The actual % of productivity that was delivered by the workers. It ranges from 0-1.
                    """
                )
        with st.container():
            st.header("Need Developer's Help?")
            st_lottie(lottie_code3, height=300, key="coding3")
            st.write(
                """
                - Name : Supun Sulakshana
                - Address : Galmatta, Walagedara, Mathugama, Sri Lanaka
                - Contact No : (+94) 71 132 7 510
                - Gmail Address : supunsulak20@gmail.com
                - Linkedin : www.linkedin.com/in/supun-sulakshana-41997a1a3
                - Twitter : https://twitter.com/SupunSulakshan3
                
                """
            )


    # st.subheader('ABC GARMENT')



if __name__ == '__main__':
    main()
