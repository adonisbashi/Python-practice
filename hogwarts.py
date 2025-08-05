'''
students = {"Hermione": "Gryffindor",
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"}

for student in students:
    print(student,  students[student], sep=", ")

'''
'''
for student in students:
    print(student)
'''




'''
for i in range(len(students)):
    print(i + 1, students[i])
'''
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russsel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "none"}
]

for student in students:
    print(student["house"], student["patronus"], sep=", ")