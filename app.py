# ==============================================================================
# Task 8: Simple Data Filtering (Streamlit version)
# Run with:  streamlit run app.py
# ==============================================================================
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Simple Data Filtering", page_icon="🎓", layout="wide")

# 1. Deliverable 1: Student records (List of Dictionaries)
students = [
    {"id": 101, "name": "Aarav",   "age": 20, "marks": 85, "department": "AI & ML"},
    {"id": 102, "name": "Bhavya",  "age": 22, "marks": 68, "department": "Data Science"},
    {"id": 103, "name": "Chirag",  "age": 19, "marks": 92, "department": "AI & ML"},
    {"id": 104, "name": "Divya",   "age": 21, "marks": 74, "department": "Computer Science"},
    {"id": 105, "name": "Eshwar",  "age": 23, "marks": 88, "department": "AI & ML"},
    {"id": 106, "name": "Fatima",  "age": 20, "marks": 59, "department": "Data Science"},
    {"id": 107, "name": "Gaurav",  "age": 22, "marks": 91, "department": "Computer Science"},
]


def display_students(title, student_list):
    """Show filtered results on the web page (not with print)."""
    st.subheader(f"{title} (Total: {len(student_list)})")
    if not student_list:
        st.warning("No matching students found.")
        return
    st.dataframe(pd.DataFrame(student_list), use_container_width=True, hide_index=True)


st.title("🎓 Task 8: Simple Data Filtering")
st.caption("Filter student records by marks, age, or department.")

# 2. Deliverable 2: Filtering operations (fixed conditions)
high_scorers = [s for s in students if s["marks"] >= 80]
ai_ml_students = [s for s in students if s["department"] == "AI & ML"]
young_students = [s for s in students if s["age"] <= 21]
top_young_aiml = [
    s for s in students
    if s["department"] == "AI & ML" and s["marks"] >= 85 and s["age"] <= 21
]

# 3. Deliverable 3: Output showing filtered students
tab1, tab2 = st.tabs(["📋 Predefined Filters", "🎛️ Interactive Filter"])

with tab1:
    display_students("All Students", students)
    display_students("Filter 1: High Scorers (Marks >= 80)", high_scorers)
    display_students("Filter 2: Department == 'AI & ML'", ai_ml_students)
    display_students("Filter 3: Age <= 21", young_students)
    display_students("Filter 4 (Combined): AI & ML, Marks >= 85, Age <= 21", top_young_aiml)

with tab2:
    departments = sorted({s["department"] for s in students})
    col1, col2, col3 = st.columns(3)
    with col1:
        selected_depts = st.multiselect("Department", departments, default=departments)
    with col2:
        min_marks = st.slider("Minimum marks", 0, 100, 0)
    with col3:
        max_age = st.slider("Maximum age", 18, 25, 25)

    custom = [
        s for s in students
        if s["department"] in selected_depts
        and s["marks"] >= min_marks
        and s["age"] <= max_age
    ]
    display_students("Your Custom Filter", custom)
