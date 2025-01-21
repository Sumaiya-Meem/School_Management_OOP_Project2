from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("XYZ High School", "Barishal")

# Adding Classroom
seventh = ClassRoom("Seventh")
eighth = ClassRoom("Eighth")
ninth = ClassRoom("Ninth")

school.add_classroom(seventh)
school.add_classroom(eighth)
school.add_classroom(ninth)

# Adding Students
amin = Student("Amin", seventh)
samin = Student("Samin", eighth)
jamin = Student("Jamin", ninth)
tamin = Student("Tamin", ninth)

school.student_admission(amin)
school.student_admission(samin)
school.student_admission(jamin)
school.student_admission(tamin)

# Adding Teachers
kamal = Teacher("Kamal Ahmed")
jamal = Teacher("Jamal Uddin")
tamal = Teacher("Tamal Hossain")

# Adding Subjects
english = Subject("English", kamal)
math = Subject("Mathematics", jamal)
science = Subject("Science", tamal)
history = Subject("History", tamal)

seventh.add_subject(english)
seventh.add_subject(math)
seventh.add_subject(science)
eighth.add_subject(history)
eighth.add_subject(math)
eighth.add_subject(science)
ninth.add_subject(science)
ninth.add_subject(math)
ninth.add_subject(english)
ninth.add_subject(history)

seventh.take_semester_final_exam()
eighth.take_semester_final_exam()
ninth.take_semester_final_exam()

print(school)
