class Student:
    pass


one = Student()     # object of Student class created
two = Student()
# adding details to object one of student class
one.name = "Riya"
one.standard = "10"
one.section = "A"
# adding details to object two of student class
two.name = "Meera"
two.standard = "12"
two.section = "B"
two.subject = ["Maths", "Science", "English"]

# printing details of both objects
print(one.name)
print(one.name, one.standard, one.section)
print(two.subject)
