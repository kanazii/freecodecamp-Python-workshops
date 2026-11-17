
class GradeManager:
    def __init__(self):
        self.students = [
            {"name": "John", "Cat 1": 12, "cat2": 15, "exam": 56}
        ]

    # Add a new student
    def add_student(self):
        stud_name = input("Enter student name: ")
        cat1 = int(input("Enter CAT 1 score: "))
        cat2 = int(input("Enter CAT 2 score: "))
        exam = int(input("Enter exam score: "))

        self.students.append({
            "name": stud_name,
            "Cat 1": cat1,
            "cat2": cat2,
            "exam": exam
        })

        print(f"{stud_name} added successfully!")

    # Calculate total marks
    def calculate_total(self):
        for student in self.students:
            total = student["Cat 1"] + student["cat2"] + student["exam"]
            student["total"] = total

 
    def display(self):
        self.calculate_total()
        self.grading()
        for student in self.students:
            print("-" * 30)
            print(f"Name: {student['name']}")
            print(f"CAT 1: {student['Cat 1']}")
            print(f"CAT 2: {student['cat2']}")
            print(f"Exam: {student['exam']}")
            print(f"Total: {student['total']}/100")
            print(f"Grade: ")




