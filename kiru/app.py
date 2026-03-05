import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="ML Intrusion Detection System", page_icon="🛡️", layout="wide")

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1c1c1c);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: white;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        transition: 0.4s ease-in-out;
        margin-bottom: 20px;
    }

    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.4);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 18px;
        text-align: center;
        opacity: 0.8;
        margin-bottom: 40px;
    }

    .footer {
        text-align: center;
        padding: 20px;
        font-size: 14px;
        opacity: 0.7;
    }
    </style>
    """, unsafe_allow_html=True)

def sidebar():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Intrusion Detection", "About"])
    return page

def hero_section():
    st.markdown('<div class="hero-title">Machine Learning Based Intrusion Detection System</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Real-Time Cyber Threat Detection Using ML Models</div>', unsafe_allow_html=True)

def dummy_model_prediction(features):
    classes = ["Normal", "DoS", "Probe", "BruteForce"]
    return np.random.choice(classes)

def intrusion_page():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Enter Network Traffic Details")

    duration = st.number_input("Connection Duration", min_value=0.0, value=10.0)
    src_bytes = st.number_input("Source Bytes", min_value=0.0, value=500.0)
    dst_bytes = st.number_input("Destination Bytes", min_value=0.0, value=300.0)
    wrong_fragment = st.number_input("Wrong Fragment", min_value=0.0, value=0.0)
    urgent = st.number_input("Urgent Packets", min_value=0.0, value=0.0)

    predict_button = st.button("Detect Intrusion")

    st.markdown('</div>', unsafe_allow_html=True)

    if predict_button:
        with st.spinner("Analyzing network traffic..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress.progress(i + 1)

        features = [duration, src_bytes, dst_bytes, wrong_fragment, urgent]
        prediction = dummy_model_prediction(features)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Detection Result")

        if prediction == "Normal":
            st.success(f"Traffic Status: {prediction}")
        else:
            st.error(f"Traffic Status: {prediction} Attack Detected")

        st.markdown('</div>', unsafe_allow_html=True)

def about_page():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("Project Overview")
    st.write("""
    This project implements a Machine Learning based Intrusion Detection System (IDS)
    to classify network traffic into Normal or Attack categories such as DoS,
    Probe, and BruteForce using trained ML algorithms.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

def footer():
    st.markdown('<div class="footer">© 2026 ML Intrusion Detection System | Developed using Streamlit</div>', unsafe_allow_html=True)

def main():
    load_css()
    page = sidebar()
    hero_section()

    if page == "Home":
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.subheader("Welcome")
        st.write("Use the sidebar to navigate to the Intrusion Detection module.")
        st.markdown('</div>', unsafe_allow_html=True)

    elif page == "Intrusion Detection":
        intrusion_page()

    elif page == "About":
        about_page()

    footer()

if __name__ == "__main__":
    main()