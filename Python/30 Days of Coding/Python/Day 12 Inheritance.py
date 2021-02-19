class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, id, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.scores = scores

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.id)
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        scorepoints = 0
        x = 0
        for score in self.scores:
            scorepoints = scorepoints + score
            x = x + 1
        averagescore = scorepoints / x    
        if averagescore >= 90 and averagescore <= 100:
            return "O"
        elif averagescore >= 80 and averagescore < 90:
            return "E"
        elif averagescore >= 70 and averagescore < 80:
            return "A"
        elif averagescore >= 55 and averagescore < 70:
            return "P"
        elif averagescore >= 40 and averagescore < 55:
            return "D"
        elif averagescore < 40:
            return "T"
line = input().split()