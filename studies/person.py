
#class definition
class Person:

    #property    
    name = 'henry'
    age = 32

    #initilize
    def __init__(self):
        self.name = 'henry2'
        self.age = 30
   

    @staticmethod
    def greet(name):
        print(f"hi {name}, nice to see you")


    def run(self):
        print("I can run as fast I can")



