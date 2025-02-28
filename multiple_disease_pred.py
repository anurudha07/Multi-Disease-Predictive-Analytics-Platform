# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:57:56 2025

@author: ANURUDHA SARKAR
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Support",
                   layout="wide",
                   page_icon="♾️")

working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('D:/Multiple Dissease Prediction Platform/Saved Models/diabetes_model.sav','rb'))
heart_disease_model = pickle.load(open('D:/Multiple Dissease Prediction Platform/Saved Models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('D:/Multiple Dissease Prediction Platform/Saved Models/parkinsons_model.sav','rb'))
breast_cancer_model = pickle.load(open('D:/Multiple Dissease Prediction Platform/Saved Models/breast_cancer_model.sav','rb'))

# sidebar
with st.sidebar:
    selected = option_menu('Multi-Disease Predictive Analytics Platform',

                           ['Diabetes',
                            'Heart Disease',
                            'Parkinsons',
                            'Breast Cancer'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'triangle'],
                           default_index=0)


# Diabetes Prediction
if selected == 'Diabetes':

    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
        
    # code for Prediction
    diab_diagnosis = ''

    # creating button

    if st.button('Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'Diabetes Detected'
        else:
            diab_diagnosis = 'Normal'

    st.success(diab_diagnosis)

# Heart Disease Prediction
if selected == 'Heart Disease':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating button

    if st.button('Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'Heart Disease Detected'
        else:
            heart_diagnosis = 'Normal'

    st.success(heart_diagnosis)

# Parkinson's Prediction
if selected == "Parkinsons":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating button    
    if st.button("Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "Parkinson's Disease Detected"
        else:
            parkinsons_diagnosis = "Normal"

    st.success(parkinsons_diagnosis)
    
#Breast Cancer Prediction
if selected == "Breast Cancer":

    # page title
    st.title("Breast Cancer Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        radm = st.text_input('radius_mean')

    with col2:
        texm = st.text_input('texture_mean')

    with col3:
        perim = st.text_input('perimeter_mean')

    with col4:
        aream = st.text_input('area_mean')

    with col5:
        smoo = st.text_input('smoothness_mean')

    with col1:
        compact_m = st.text_input('compactness_mean')

    with col2:
        concavity_m = st.text_input('concavity_mean')

    with col3:
        cpm = st.text_input('concave points_mean')

    with col4:
        sm = st.text_input('symmetry_mean')

    with col5:
        fdm = st.text_input('fractal_dimension_mean')

    with col1:
        rad = st.text_input('radius_se')

    with col2:
        tex = st.text_input('texture_se')

    with col3:
        peri = st.text_input('perimeter_se')

    with col4:
        area = st.text_input('area_se')

    with col5:
        smt = st.text_input('smoothness_se')

    with col1:
        compt = st.text_input('compactness_se')

    with col2:
        concavity = st.text_input('concavity_se')

    with col3:
        cp = st.text_input('concave points_se')

    with col4:
        sym = st.text_input('symmetry_se')

    with col5:
        fds = st.text_input('fractal_dimension_se')
        
    with col1:
        rw = st.text_input('radius_worst')

    with col2:
        tw = st.text_input('texture_worst')
   
    with col3:
         pw = st.text_input('perimeter_worst')

    with col4:
         aw = st.text_input('area_worst')

    with col5:
         sw = st.text_input('smoothness_worst')
    
    with col1:
        cw = st.text_input('compactness_worst')

    with col2:
        concavity_w = st.text_input('concavity_worst')

    with col3:
        cpw = st.text_input('concave points_worst')

    with col4:
        sworst = st.text_input('symmetry_worst')

    with col5:
        fdw = st.text_input('fractal_dimension_worst')
    
    
         
     

    # code for Prediction
    breast_cancer_diagnosis = ''

    # creating button    
    if st.button("Test Result"):

        user_input = [radm, texm, perim, aream, smoo,
                      compact_m, concavity_m, cpm, sm, fdm,
                      rad, tex, peri, area, smt,
                      compt, concavity, cp, sym, fds,
                      rw, tw, pw, aw, sw,
                      cw, concavity_w, cpw, sworst, fdw]
        user_input = [float(x) for x in user_input]

        b_cancer_prediction = breast_cancer_model.predict([user_input])

        if b_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "Breast Cancer Detected"
        else:
            breast_cancer_diagnosis = "Normal"

    st.success(breast_cancer_diagnosis)
