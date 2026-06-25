# Student Marks Analysis

A beginner-friendly Data Analysis project that explores student performance data using Python, Pandas, and Matplotlib.

This project demonstrates how to inspect datasets, calculate statistics, identify high-performing and low-performing students, and create visualizations for better understanding of academic performance.

---

## Project Objective

The objective of this project is to analyze student marks and answer questions such as:

- What is the average score in each subject?
- Which students scored exceptionally high?
- Which students require improvement?
- How are marks distributed across students?

---

## Project Structure

```text
Student_Marks_Analysis
├── average.png
├── findings_and_observations.docx
├── Maths_marks_distribution.png
├── student_marks_analyis.py
├── student_marks_analysis.pptx
└── students.csv
```

---

## Dataset

**File:** `students.csv`

The dataset contains student names and marks obtained in various subjects.

Example columns:

```text
Name
Maths
Science
English
```

---

## Technologies Used

- Python
- Pandas
- Matplotlib

---

## Analysis Performed

### 1. Dataset Inspection

The dataset is inspected using:

```python
df.head()
df.info()
df.describe()
```

This helps understand:

- Number of records
- Data types
- Missing values
- Statistical summary

---

### 2. Average Marks Analysis

Average marks for all numeric subjects are calculated using:

```python
avg_marks = df.mean(numeric_only=True)
```

The results are visualized using a bar chart.

Output:

```text
average.png
```

---

### 3. High Performing Students

Students scoring more than 90 marks in Mathematics are identified using:

```python
df[df["Maths"] > 90]
```

This helps identify top-performing students.

---

### 4. Students Needing Improvement

Students scoring below 30 marks in Mathematics are identified using:

```python
df[df["Maths"] < 30]
```

This helps identify students who may require additional support.

---

### 5. Marks Distribution Analysis

A histogram is created to visualize the spread of Mathematics marks.

```python
plt.hist(df["Maths"])
```

Output:

```text
Maths_marks_distribution.png
```

This helps understand:

- Distribution of marks
- Concentration of students
- Performance trends
- Score spread

---

## Visualizations

### Average Marks by Subject

**File:** `average.png`

Displays the average marks obtained in each subject.

### Mathematics Marks Distribution

**File:** `Maths_marks_distribution.png`

Shows how Mathematics marks are distributed among students.

---

## Key Findings

- Average marks can be quickly compared across subjects.
- High-performing students can be identified using filtering conditions.
- Students scoring below expectations can be highlighted for improvement.
- Histograms reveal how marks are distributed and whether scores are concentrated in specific ranges.

---

## Supporting Materials

### Presentation

`student_marks_analysis.pptx`

Project presentation used during the tutorial.

### Findings Report

`findings_and_observations.docx`

Contains observations and conclusions derived from the analysis.

---

## Learning Outcomes

By completing this project, learners will understand:

- Reading CSV files with Pandas
- Inspecting datasets
- Descriptive statistics
- Data filtering
- Bar chart creation
- Histogram creation
- Basic data storytelling

---

## YouTube Tutorial

This project is explained step-by-step on my YouTube channel:

📺 https://youtube.com/@ssutradhar35

---

## Author

**Subir Sutradhar**
