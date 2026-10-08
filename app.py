# ==============================================================================
# Task 8: Simple Data Filtering
# ==============================================================================

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
    """Helper function to cleanly display filtered results."""
    print(f"\n--- {title} (Total: {len(student_list)}) ---")
    if not student_list:
        print("No matching students found.")
        return
    for s in student_list:
        print(f"ID: {s['id']} | Name: {s['name']:<8} | Age: {s['age']} | "
              f"Marks: {s['marks']} | Dept: {s['department']}")


# ==============================================================================
# 2. Deliverable 2: Filtering Operations
# ==============================================================================

# Condition A: marks greater than or equal to 80
high_scorers = [s for s in students if s["marks"] >= 80]

# Condition B: students in the 'AI & ML' department
ai_ml_students = [s for s in students if s["department"] == "AI & ML"]

# Condition C: students aged 21 or younger
young_students = [s for s in students if s["age"] <= 21]

# Condition D (Combined): 'AI & ML' AND marks >= 85 AND age <= 21
top_young_aiml = [
    s for s in students
    if s["department"] == "AI & ML" and s["marks"] >= 85 and s["age"] <= 21
]


# ==============================================================================
# 3. Deliverable 3: Output Showing Filtered Students
# ==============================================================================

if __name__ == "__main__":
    display_students("All Students", students)
    display_students("Filter 1: High Scorers (Marks >= 80)", high_scorers)
    display_students("Filter 2: Department == 'AI & ML'", ai_ml_students)
    display_students("Filter 3: Age <= 21", young_students)
    display_students("Filter 4 (Combined): AI & ML, Marks >= 85, Age <= 21", top_young_aiml)
