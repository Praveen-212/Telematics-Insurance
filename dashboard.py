import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Telematics Dashboard", layout="centered")
st.title("🚗 Telematics-Based Usage Insurance (Live Dashboard)")

risk_scores = []
base_premium = 5000

placeholder = st.empty()

for i in range(20):
    d = pd.DataFrame({
        'speed': [np.random.normal(60, 15)],
        'acceleration': [np.random.normal(0, 3)],
        'braking': [np.random.normal(0, 4)],
        'cornering': [np.random.normal(0, 2)],
        'timestamp': [pd.to_datetime('now')]
    })

    def analyze(row):
        score = 0
        if abs(row['acceleration']) > 3: score += 1
        if abs(row['braking']) > 5: score += 2
        if abs(row['cornering']) > 3: score += 1
        if row['speed'] > 90: score += 1
        return score

    score = analyze(d.iloc[0])
    risk_scores.append(score)
    avg_risk = np.mean(risk_scores)

    if avg_risk < 1:
        adj = -0.1
    elif avg_risk < 2:
        adj = 0
    else:
        adj = 0.25

    final_premium = base_premium * (1 + adj)

    if avg_risk < 1:
        fb = "Excellent driving!"
    elif avg_risk < 2:
        fb = "Drive safe — some risky behavior."
    else:
        fb = "⚠️ High risk detected. Improve safety!"

    with placeholder.container():
        st.metric("Speed (km/h)", f"{d['speed'].iloc[0]:.2f}")
        st.metric("Current Risk Score", f"{score}")
        st.metric("Average Risk Score", f"{avg_risk:.2f}")
        st.metric("Premium (₹)", f"{final_premium:.2f}")
        st.info(fb)
    
    time.sleep(1)
