# app/streamlit_app.py

import streamlit as st

from src.recommend import get_dummy_recommendation
from src.utils import format_currency

st.title("Surgical Waste Reduction ML Platform (Prototype)")

st.write(
    "This prototype simulates a machine-learning tool that predicts surgical supply "
    "waste and recommends optimized kit configurations."
)

procedure_name = st.selectbox(
    "Select a procedure",
    [
        "Laparoscopic Cholecystectomy",
        "Total Knee Replacement",
        "Appendectomy",
    ],
)

if st.button("Get Waste Prediction and Recommendations"):
    result = get_dummy_recommendation(procedure_name)

    st.subheader(f"Procedure: {result['procedure_name']}")
    st.write("Predicted Waste Cost:", format_currency(result["predicted_waste_cost"]))
    st.write("High Waste Risk:", f"{result['high_waste_risk'] * 100:.1f}%")

    st.subheader("Recommended Kit Changes")
    for rec in result["recommendations"]:
        st.write(
            f"- {rec['item']}: current {rec['current_planned']}, "
            f"recommended {rec['recommended_planned']} "
            f"(savings ~ {format_currency(rec['expected_annual_savings'])}/year)"
        )

st.info("Note: This is an early prototype using placeholder data and logic.")
