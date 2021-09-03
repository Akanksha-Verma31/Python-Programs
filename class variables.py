class Student:
    # class variables are the variables which we declare inside a class
    no_of_subjects = 5
    pass


one = Student()
two = Student()

one.name = "A"
one.standard = "11"
one.section = "C"

two.name = "B"
two.standard = "12"
two.section = "C"

print(one.name)
print(Student.no_of_subjects)
print(one.no_of_subjects)     # we can access the class variable either through class name or class obj
