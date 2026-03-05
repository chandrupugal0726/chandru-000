import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Intrusion Detection System",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------
encoder = joblib.load("encoder.pkl")
model = joblib.load("model.pkl")

# -----------------------------
# CUSTOM CSS (Professional UI)
# -----------------------------
st.markdown("""
<style>

body {
    background-color: #0f172a;
}

.main-title {
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color:#0ea5e9;
}

.subtitle {
    text-align:center;
    font-size:18px;
    color:#94a3b8;
    margin-bottom:30px;
}

.card {
    background-color:#1e293b;
    padding:30px;
    border-radius:15px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.4);
}

.result-normal{
    background-color:#064e3b;
    padding:20px;
    border-radius:10px;
    font-size:24px;
    color:#34d399;
    text-align:center;
}

.result-attack{
    background-color:#7f1d1d;
    padding:20px;
    border-radius:10px;
    font-size:24px;
    color:#f87171;
    text-align:center;
}

.footer{
    text-align:center;
    margin-top:40px;
    color:#94a3b8;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown('<div class="main-title">🛡️ Intrusion Detection System</div>', unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Machine Learning based Network Threat Detection Platform</div>',
unsafe_allow_html=True
)

# -----------------------------
# INPUT SECTION
# -----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    duration = st.number_input("Duration", min_value=0.0)

    src_bytes = st.number_input("Source Bytes", min_value=0.0)

    wrong_fragment = st.number_input("Wrong Fragment", min_value=0)

    protocol_type = st.selectbox(
        "Protocol Type",
        ["tcp", "udp", "icmp"]
    )

    service = st.selectbox(
        "Service",
        ["http", "ftp", "smtp", "dns", "ssh"]
    )

with col2:

    dst_bytes = st.number_input("Destination Bytes", min_value=0.0)

    urgent = st.number_input("Urgent Packets", min_value=0)

    flag = st.selectbox(
        "Flag",
        ["SF", "S0", "REJ", "RSTR"]
    )

    count = st.number_input("Count", min_value=0)

    srv_count = st.number_input("Srv Count", min_value=0)

predict_button = st.button("🔍 Analyze Network Traffic")

st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# PREDICTION
# -----------------------------
if predict_button:

    # Input dataframe
    input_df = pd.DataFrame({
        "duration":[duration],
        "protocol_type":[protocol_type],
        "service":[service],
        "flag":[flag],
        "src_bytes":[src_bytes],
        "dst_bytes":[dst_bytes],
        "wrong_fragment":[wrong_fragment],
        "urgent":[urgent],
        "count":[count],
        "srv_count":[srv_count]
    })

    # Categorical columns
    cat_cols = ["protocol_type","service","flag"]

    # Encode
    encoded = encoder.transform(input_df[cat_cols])

    encoded_df = pd.DataFrame(
        encoded,
        columns=encoder.get_feature_names_out(cat_cols)
    )

    # Drop categorical
    input_df = input_df.drop(columns=cat_cols)

    # Combine
    final_df = pd.concat([input_df, encoded_df], axis=1)

    # Predict
    prediction = model.predict(final_df)[0]

    st.write("")

    # Show Result
    if prediction == 0:
        st.markdown(
        '<div class="result-normal">✅ Normal Network Traffic</div>',
        unsafe_allow_html=True
        )
    else:
        st.markdown(
        '<div class="result-attack">🚨 Intrusion Attack Detected</div>',
        unsafe_allow_html=True
        )

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
'<div class="footer">Machine Learning Intrusion Detection System | Built with Streamlit</div>',
unsafe_allow_html=True
)