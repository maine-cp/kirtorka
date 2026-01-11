class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return f"{self.name} is {self.age} and studies: {', '.join(self.subjects)}"



students = []

alice = Student("Alice", 15, ["Math", "Science"])
bob = Student("Bob", 16, ["History"])
charlie = Student("Charlie", 15, ["Physics"])
diana = Student("Diana", 17, ["Biology"])


students.append(alice)
students.append(bob)
students.append(charlie)
students.append(diana)


print("Number of students:", len(students))


name_to_remove = "Bob"
students = [s for s in students if s.name != name_to_remove]

print("After removal:")
for s in students:
    print(s.get_info())



grades = {}

grades["Alice"] = 90
grades["Charlie"] = 85
grades["Diana"] = 92

grades["Charlie"] = 88
print("Updated grade for Charlie:", grades["Charlie"])

for name, grade in grades.items():
    print(f"Student: {name}, Grade: {grade}")




schedule = ("Math", "Lunch", "Science", "Gym")


print("Second element:", schedule[1])

try:
    schedule[1] = "Break"
except TypeError as e:
    print("Error:", e)



classes = {"Robotics", "Debate", "Art"}


classes.add("Math")
classes.add("Art")  
print("Classes set:", classes)


if "Robotics" in classes:
    print("Robotics is in the set")
else:
    print("Robotics is not in the set")

morning_classes = {"Math", "Science", "Robotics"}
afternoon_classes = {"Art", "Math", "Gym"}

common_classes = morning_classes & afternoon_classes
print("Common classes:", common_classes)
