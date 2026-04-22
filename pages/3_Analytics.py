
import streamlit as st
import pandas as pd

st.title("Analytics")

df = pd.DataFrame({
    "CGPA":[6,7,8,9],
    "Placement":[40,60,80,95]
})

st.line_chart(df.set_index("CGPA"))
