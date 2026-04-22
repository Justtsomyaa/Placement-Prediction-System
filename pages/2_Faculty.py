
import streamlit as st
import pandas as pd

st.title("Faculty Dashboard")

data = pd.DataFrame({
    "Name":["Aman","Riya","Karan","Neha","Arjun"],
    "CGPA":[6.5,8.2,5.9,7.1,6.0],
    "Risk":["High","Low","High","Medium","High"]
})

search = st.text_input("Search")
risk = st.selectbox("Filter", ["All","High","Medium","Low"])

df = data

if search:
    df = df[df["Name"].str.contains(search, case=False)]

if risk != "All":
    df = df[df["Risk"]==risk]

st.dataframe(df)

csv = df.to_csv(index=False)
st.download_button("Download CSV", csv, "report.csv")
