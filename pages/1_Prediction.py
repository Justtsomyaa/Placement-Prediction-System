
import streamlit as st

st.title("Placement Prediction")

mode = st.radio("Choose Mode", ["General Prediction", "Role-Based Prediction"])

cgpa = st.slider("CGPA", 0.0, 10.0, 7.0)
intern = st.slider("Internships", 0, 5, 1)
projects = st.slider("Projects", 0, 5, 2)
apt = st.slider("Aptitude Score", 0, 100, 60)
soft = st.slider("Soft Skills", 1, 10, 5)

if mode == "Role-Based Prediction":
    role = st.selectbox("Select Role", ["Data Analyst","Software Developer","ML Engineer","Web Developer"])

    role_weights = {
        "Data Analyst":{"cgpa":0.2,"aptitude":0.4,"projects":0.2,"internships":0.1,"soft_skills":0.1},
        "Software Developer":{"cgpa":0.2,"projects":0.3,"internships":0.2,"aptitude":0.2,"soft_skills":0.1},
        "ML Engineer":{"cgpa":0.3,"projects":0.3,"aptitude":0.2,"internships":0.1,"soft_skills":0.1},
        "Web Developer":{"cgpa":0.2,"projects":0.3,"internships":0.2,"aptitude":0.2,"soft_skills":0.1}
    }

if st.button("Predict"):
    if mode == "General Prediction":
        score = (cgpa/10)*0.3 + (apt/100)*0.3 + (intern/5)*0.2 + (projects/5)*0.1 + (soft/10)*0.1
    else:
        w = role_weights[role]
        score = (cgpa/10)*w["cgpa"] + (apt/100)*w["aptitude"] + (projects/5)*w["projects"] + (intern/5)*w["internships"] + (soft/10)*w["soft_skills"]

    st.progress(int(score*100))

    if score > 0.7:
        st.success("High Probability")
    elif score > 0.5:
        st.warning("Moderate")
    else:
        st.error("Low")

    if mode == "Role-Based Prediction":
        st.subheader("Suggestions")
        if projects < 2:
            st.write("- Increase projects")
        if intern == 0:
            st.write("- Do internship")
        if apt < 60:
            st.write("- Improve aptitude")
