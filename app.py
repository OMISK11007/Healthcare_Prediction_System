import streamlit as st
import pandas as pd
from datetime import datetime
from healthcare import DengueDecisionSystem, get_mock_data 

st.set_page_config(page_title="Dengue Decision Support", page_icon="🏥", layout="wide")
st.title("🏥 Dengue Decision Support System")

if 'history' not in st.session_state:
    st.session_state.history = []

@st.cache_resource
def load_system():
    sys = DengueDecisionSystem()
    df = get_mock_data()
    sys.train(df)
    return sys

system = load_system()

# Inputs
st.sidebar.header("Patient Vitals")
age = st.sidebar.slider("Age", 1, 100, 25)
fever = st.sidebar.slider("Days of Fever", 1, 14, 3)
plt_count = st.sidebar.number_input("Platelet Count", value=150000)
hct = st.sidebar.slider("Hematocrit %", 30, 60, 40)
warnings = st.sidebar.selectbox("Warning Signs", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

if st.button("Analyze Risk", type="primary"):
    patient_df = pd.DataFrame([[age, fever, plt_count, hct, warnings]], 
                              columns=['age', 'days_of_fever', 'platelet_count', 'hematocrit_pct', 'warning_signs'])
    
    result, risk_val = system.classify_patient(patient_df)
    
    st.subheader("Clinical Recommendation:")
    if "CRITICAL" in result: st.error(result)
    elif "HIGH" in result: st.warning(result)
    else: st.success(result)

    st.write(f"**Model Risk Confidence:** {risk_val:.1%}")
    st.progress(risk_val)

    # Graph
    st.subheader("📈 Platelet vs. Risk Trend")
    trend_df = system.get_risk_trend(patient_df)
    st.line_chart(trend_df.set_index("Platelet Count"))

    # History
    st.session_state.history.append({"Time": datetime.now().strftime("%H:%M"), "Age": age, "Result": result})

if st.session_state.history:
    st.divider()
    st.subheader("📋 Session History")
    st.table(pd.DataFrame(st.session_state.history))