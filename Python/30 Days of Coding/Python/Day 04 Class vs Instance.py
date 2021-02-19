class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if age < 0:
            print("Age is not valid, setting age to 0.")
            p = 0
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13:
            print("You are young.")
        elif age >= 13 and age < 18:
            print("You are a teenager.")
        elif age >= 18:
            print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age = age + 1

t = int(input())