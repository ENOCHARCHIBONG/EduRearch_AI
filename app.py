
import streamlit as st
import json
from math_solver import solve_linear_equation

# Page settings
st.set_page_config(page_title="EduReach AI - Math Tutor", layout="centered")

st.title("📚 EduReach AI - Mathematics Learning")
st.write("Offline learning platform for secondary school students.")

# ✅ LOAD JSON FILES (THIS WAS MISSING)
with open("notes.json") as f:
    notes = json.load(f)

with open("questions.json") as f:
    questions = json.load(f)

# Sidebar topic selection
topic = st.sidebar.selectbox("Select Topic", list(notes.keys()))

# Tabs
tab1, tab2, tab3 = st.tabs(["📘 Learn", "📝 Quiz", "🤖 AI Tutor"])

# 📘 Learn Tab
with tab1:
    st.header(f"Topic: {topic}")
    st.write(notes.get(topic, "No notes available"))

# 📝 Quiz Tab
with tab2:
    if topic in questions:
        st.header("Quiz")
        user_answers = []

        for i, q in enumerate(questions[topic]):
            ans = st.radio(f"Q{i+1}: {q['question']}", q['options'], key=f"{topic}_{i}")
            user_answers.append((ans, q['answer']))

        if st.button("Submit Quiz"):
            score = sum(1 for u, a in user_answers if u == a)
            st.success(f"Score: {score}/{len(user_answers)}")

            if score < len(user_answers)/2:
                st.warning("⚠️ You need more practice")
            else:
                st.balloons()
                st.success("🎉 Great job!")

# 🤖 AI Tutor Tab
with tab3:
    st.header(f"AI Tutor - {topic}")

    # ALGEBRA
    if topic == "Algebra":
        eq = st.text_input("Enter equation (e.g., 2x + 3 = 7)")
        
        if st.button("Solve"):
            if eq:
                result = solve_linear_equation(eq)
                st.code(result)

    # GEOMETRY
    elif topic == "Geometry":
        base = st.number_input("Enter base", value=0.0)
        height = st.number_input("Enter height", value=0.0)

        if st.button("Calculate Area"):
            area = 0.5 * base * height
            st.success(f"Area of triangle = {area}")

    # TRIGONOMETRY
    elif topic == "Trigonometry":
        import math
        angle = st.number_input("Enter angle (degrees)", value=0.0)

        if st.button("Calculate sin(θ)"):
            result = math.sin(math.radians(angle))
            st.success(f"sin({angle}) = {round(result, 3)}")

    # STATISTICS
    elif topic == "Statistics":
        numbers = st.text_input("Enter numbers separated by commas (e.g., 2,4,6)")

        if st.button("Calculate Mean"):
            if numbers:
                nums = [float(n) for n in numbers.split(",")]
                mean = sum(nums) / len(nums)
                st.success(f"Mean = {mean}")

    # PROBABILITY
    elif topic == "Probability":
        favorable = st.number_input("Favorable outcomes", value=0.0)
        total = st.number_input("Total outcomes", value=1.0)

        if st.button("Calculate Probability"):
            if total != 0:
                prob = favorable / total
                st.success(f"Probability = {prob}")

    else:
        st.write("AI tutor support coming soon for this topic!")
