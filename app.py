import streamlit as st

def get_learning_advice(quiz_scores):
    advice = {}
    for subject, score in quiz_scores.items():
        if score >= 80:
            advice[subject] = "🌟 Excellent! Try advanced materials or challenge questions."
        elif 60 <= score < 80:
            advice[subject] = "👍 Good! Review notes and practice more to improve."
        else:
            advice[subject] = "⚠️ Needs improvement. Focus on basics and revise thoroughly."
    return advice

st.title("📊 Learning Advice Recommendation System")
st.subheader("Enter your quiz scores:")

subjects = st.text_input("Subjects (comma separated)", "Math, Science, English")
subject_list = [s.strip() for s in subjects.split(",") if s.strip()]

quiz_scores = {}
for subject in subject_list:
    score = st.slider(f"{subject} Score", 0, 100, 60)
    quiz_scores[subject] = score

if st.button("Get Recommendations"):
    st.write("### 📘 Personalized Learning Advice:")
    recommendations = get_learning_advice(quiz_scores)
    for subject, tip in recommendations.items():
        st.markdown(f"**{subject}**: {tip}")
