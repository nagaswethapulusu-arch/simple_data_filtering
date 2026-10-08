# Task 8: Simple Data Filtering

**Track:** AI & ML | **Level 1 · Day 8**

## Description
A small Python program that stores student records as a list of dictionaries
and filters them by marks, age, and department using conditional statements.

## Objective
Understand how conditions can be used to filter structured data.

## Tools
- Python 3.8+
- Jupyter Notebook (optional – the code can be pasted cell-by-cell)

## Project Structure
```
.
├── app.py             # Student records, filters, and output
├── requirements.txt   # Optional extras (app.py needs no external packages)
└── README.md
```

## How to Run
```bash
# (optional) install extras for Jupyter / Pandas
pip install -r requirements.txt

# run the program
python app.py
```
In Jupyter: run `jupyter notebook`, create a new notebook, and paste the
contents of `app.py` into cells.

## Deliverables

### 1. Student Records
Seven records stored as a list of dictionaries, each with `id`, `name`,
`age`, `marks`, and `department`.

### 2. Filtering Operations
| Filter | Condition | Matches |
|--------|-----------|---------|
| 1 | `marks >= 80` | 4 |
| 2 | `department == "AI & ML"` | 3 |
| 3 | `age <= 21` | 4 |
| 4 (combined) | `department == "AI & ML"` **and** `marks >= 85` **and** `age <= 21` | 2 |

Each filter uses a list comprehension, e.g.:
```python
high_scorers = [s for s in students if s["marks"] >= 80]
```

### 3. Output
```
--- Filter 1: High Scorers (Marks >= 80) (Total: 4) ---
ID: 101 | Name: Aarav    | Age: 20 | Marks: 85 | Dept: AI & ML
ID: 103 | Name: Chirag   | Age: 19 | Marks: 92 | Dept: AI & ML
ID: 105 | Name: Eshwar   | Age: 23 | Marks: 88 | Dept: AI & ML
ID: 107 | Name: Gaurav   | Age: 22 | Marks: 91 | Dept: Computer Science

--- Filter 2: Department == 'AI & ML' (Total: 3) ---
ID: 101 | Name: Aarav    | Age: 20 | Marks: 85 | Dept: AI & ML
ID: 103 | Name: Chirag   | Age: 19 | Marks: 92 | Dept: AI & ML
ID: 105 | Name: Eshwar   | Age: 23 | Marks: 88 | Dept: AI & ML

--- Filter 3: Age <= 21 (Total: 4) ---
ID: 101 | Name: Aarav    | Age: 20 | Marks: 85 | Dept: AI & ML
ID: 103 | Name: Chirag   | Age: 19 | Marks: 92 | Dept: AI & ML
ID: 104 | Name: Divya    | Age: 21 | Marks: 74 | Dept: Computer Science
ID: 106 | Name: Fatima   | Age: 20 | Marks: 59 | Dept: Data Science

--- Filter 4 (Combined): AI & ML, Marks >= 85, Age <= 21 (Total: 2) ---
ID: 101 | Name: Aarav    | Age: 20 | Marks: 85 | Dept: AI & ML
ID: 103 | Name: Chirag   | Age: 19 | Marks: 92 | Dept: AI & ML
```

## Interview Questions

**What is data filtering?**
Selecting only the records that satisfy one or more conditions, leaving the
original data unchanged.

**How would you filter a Pandas DataFrame?**
Use boolean indexing:
```python
import pandas as pd
df = pd.DataFrame(students)
df[(df["department"] == "AI & ML") & (df["marks"] >= 85)]
```
Use `&` (and), `|` (or), and wrap each condition in parentheses.
`df.query("marks >= 85 and age <= 21")` also works.

**What is the difference between filtering and sorting?**
Filtering *removes* rows that don't meet a condition (fewer rows out).
Sorting *reorders* rows by a column (same rows, new order).

## Key Learnings
- Lists of dictionaries are a simple way to model tabular data.
- List comprehensions with `if` give concise filtering.
- Conditions combine with `and` / `or` for more precise results.
