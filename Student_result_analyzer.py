# <-----------------------------------------------Mini Project 1 🏆--------------------------------------------------------------->
# <-------------------------------------Student Result Analyzer & Grade Report----------------------------------------------->

students = [
    {"name": "Rahul",   "marks": [85, 92, 78, 88, 95]},
    {"name": "Priya",   "marks": [72, 68, 75, 80, 70]},
    {"name": "Amit",    "marks": [45, 52, 38, 60, 42]},
    {"name": "Sneha",   "marks": [95, 98, 92, 96, 99]},
    {"name": "Rohan",   "marks": [35, 28, 42, 30, 38]},
    {"name": "Pooja",   "marks": [78, 82, 80, 75, 88]},
    {"name": "Karan",   "marks": [60, 55, 65, 58, 62]},
    {"name": "Meera",   "marks": [90, 88, 94, 92, 87]},
    {"name": "Vikram",  "marks": [25, 32, 28, 35, 30]},
    {"name": "Anjali",  "marks": [68, 72, 71, 65, 74]},
]

subjects = ["Maths", "Science", "English", "History", "Computer"]

# ─────────────────────────────────────────────
# Function to calculate grade based on percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


Total_Marks = 500

print("\n" + "=" * 60)
print("        STUDENT RESULT ANALYZER - CLASS REPORT")
print("=" * 60)

# ─────────────────────────────────────────────
# Part-1: Every Student Report
# ─────────────────────────────────────────────
print("\n-----------------INDIVIDUAL RESULTS-----------------------\n")

for student in students:
    name                = student["name"]
    marks               = student["marks"]
    total_student_marks = sum(marks)
    student_percentage  = (total_student_marks / Total_Marks) * 100
    grade               = get_grade(student_percentage)           
    print(f"Student: {name:<8} | Total: {total_student_marks}/500 | {student_percentage:.2f}% | Grade: {grade}")


# ─────────────────────────────────────────────
# Part-2: Class Report
# ─────────────────────────────────────────────
print("\n--------------------Class Summary--------------------\n")

# class topper
class_topper = max(students, key=lambda x: sum(x["marks"]))
print(f"Class Topper           : {class_topper['name']} with {sum(class_topper['marks'])} marks")

# class average percentage
total_class_marks       = sum([sum(student["marks"]) for student in students])
class_average_percentage = (total_class_marks / (Total_Marks * len(students))) * 100
print(f"Class Average          : {class_average_percentage:.2f}%")

# total students
total_students = len(students)
print(f"Total Students         : {total_students}")

# pass / fail
passed_students = [student for student in students if (sum(student["marks"]) / Total_Marks) * 100 >= 50]
failed_students = [student for student in students if (sum(student["marks"]) / Total_Marks) * 100 < 50]
print(f"Passed                 : {len(passed_students)}")
print(f"Failed                 : {len(failed_students)}")


# ─────────────────────────────────────────────
# Danger Zone
# ─────────────────────────────────────────────
print("\n--------------------- Danger Zone (F Grade Students) ----------------------\n")

danger_zone_students = [student for student in students if (sum(student["marks"]) / Total_Marks) * 100 < 50]
for student in danger_zone_students:
    pct   = (sum(student["marks"]) / Total_Marks) * 100
    grade = get_grade(pct)                                        
    print(f"{student['name']:<8} | {pct:.2f}% | Grade: {grade} | NEEDS IMMEDIATE ATTENTION!")


# ─────────────────────────────────────────────
# Part-3: Subject-wise Analysis
# ─────────────────────────────────────────────
print("\n--------------------- SUBJECT-WISE ANALYSIS ----------------------\n")

for i, subject in enumerate(subjects):
    subject_marks   = [s["marks"][i] for s in students]
    subject_average = sum(subject_marks) / len(students)
    print(f"{subject:<10} : Class Average = {subject_average:.2f}%")

min_average_subject = min(subjects, key=lambda s: sum(student["marks"][subjects.index(s)] for student in students) / len(students))
max_average_subject = max(subjects, key=lambda s: sum(student["marks"][subjects.index(s)] for student in students) / len(students))
print(f"\nToughest Subject       : {min_average_subject}")
print(f"Easiest Subject        : {max_average_subject}")


# ─────────────────────────────────────────────
# Part-4: Ranking
# ─────────────────────────────────────────────
print("\n--------------------- RANKING ----------------------\n")

ranking_students = sorted(students, key=lambda x: sum(x["marks"]) / Total_Marks * 100, reverse=True)
for rank, student in enumerate(ranking_students, start=1):
    pct   = (sum(student["marks"]) / Total_Marks) * 100
    grade = get_grade(pct)                                       
    print(f"Rank {rank:<2} | {student['name']:<8} | Total: {sum(student['marks'])}/500 | {pct:.2f}% | Grade: {grade}")

print("\n" + "=" * 60)
print("                  END OF REPORT")
print("=" * 60)

# ------------------------------------------------End of Mini Project 1 --------------------------------------------------------------