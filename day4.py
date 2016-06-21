class Person:    
    def __init__(self,initial_Age): # Add some more code to run some checks on initial_Age
        if(initial_Age<0): 
            print "Age is not valid, setting age to 0."
            initial_Age = 0
        self.age = initial_Age
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age<13: print "You are young."
        elif self.age in xrange(13,18): print "You are a teenager."
        else: print "You are old."
    def yearPasses(self):
        self.age +=1
        # Increment the age of the person in here 