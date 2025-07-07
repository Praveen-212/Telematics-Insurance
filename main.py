import pandas as pd
import numpy as np
import time
from datetime import datetime

def generate_telematics_data():
    return pd.DataFrame({
        'speed': [np.random.normal(60, 15)],
        'acceleration': [np.random.normal(0, 3)],
        'braking': [np.random.normal(0, 4)],
        'cornering': [np.random.normal(0, 2)],
        'timestamp': [pd.to_datetime('now')]
    })

def analyze_behavior(row):
    score = 0
    if abs(row['acceleration']) > 3: score += 1
    if abs(row['braking']) > 5: score += 2
    if abs(row['cornering']) > 3: score += 1
    if row['speed'] > 90: score += 1
    return score

def feedback(score):
    if score < 1:
        return "Excellent driving! Keep it up."
    elif score < 2:
        return "Safe driving, but there’s room for improvement."
    else:
        return "High risk detected. Please drive safely."

def generate_report(risk_score, premium, feedback_text):
    html = f"""
    <html>
    <head>
        <title>Insurance Report</title>
        <style>
            body {{ font-family: Arial; padding: 20px; background-color: #f5f5f5; }}
            .box {{ background: white; padding: 20px; border-radius: 8px; max-width: 500px; margin: auto; }}
            h1 {{ color: #003366; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Telematics Insurance Report</h1>
            <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Average Risk Score:</strong> {risk_score:.2f}</p>
            <p><strong>Premium:</strong> ₹{premium:.2f}</p>
            <p><strong>Feedback:</strong> {feedback_text}</p>
        </div>
    </body>
    </html>
    """
    with open("insurance_report.html", "w") as f:
        f.write(html)

def main():
    print("🚗 Starting Telematics-Based Usage Insurance System...\n")
    risk_scores = []
    base_premium = 5000

    for _ in range(20):
        d = generate_telematics_data()
        score = analyze_behavior(d.iloc[0])
        risk_scores.append(score)

        print(f"[{d['timestamp'].iloc[0]}] Speed: {d['speed'].iloc[0]:.2f} km/h | Risk Score: {score}")
        time.sleep(0.5)

    avg_risk = np.mean(risk_scores)
    if avg_risk < 1:
        adj = -0.1
    elif avg_risk < 2:
        adj = 0
    else:
        adj = 0.2

    final_premium = base_premium * (1 + adj)
    fb = feedback(avg_risk)

    print("\n✅ Final Risk Score:", avg_risk)
    print("💰 Adjusted Premium: ₹", round(final_premium, 2))
    print("📢 Feedback:", fb)

    generate_report(avg_risk, final_premium, fb)
    print("📝 HTML report saved as: insurance_report.html")

if __name__ == "__main__":
    main()
