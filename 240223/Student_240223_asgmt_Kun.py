#this is an example Student class
class Student:
    
    # assign values to the instance variables
    def __init__ (self, nm, gr, tc):
        self.name = nm
        self.grade = gr
        self.course = tc
       
    #return the name instance variable 
    def getName(self):
        return self.name
    
    #assign a value to the name instance variable
    def setName(self, nn):
        self.name = nn

    def getCourse(self):
        return self.course
    #return the entire set of instance variables
    #as one big string
    def __str__(self): 
        return "student " + self.name + "  " + str(self.grade) + " " + self.course