#comment the import line off
#and rerun the program
#it will not work without the import
from Student_240223_asgmt_Kun import *

# Creates a Student
one = Student("Xavier", 9, "History")

# prints the Student's name
print( one.getName() )

# Creates a Student
two = Student("Bob", 12, "APCompSci")

# prints the Student's name
print(two.getName())

# prints the entire Student
print(two)

three = Student("Kun", 17, "Math")

print(three)

print(three.grade)
