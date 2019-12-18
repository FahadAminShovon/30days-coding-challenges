

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
    def __init__(self,firstName,lastName,idNum,scores):
        super().__init__(firstName,lastName,idNum)
        self.scores = scores
    #
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        counter = 0
        scoress = 0
        for score in self.scores:
            scoress+=score
            counter+=1
        scoress=scoress//counter

        if(scoress<=100 and scoress>=90):return 'O'
        elif(scoress>=80):return 'E'
        elif(scoress>=70): return 'A'
        elif(scoress>=55): return 'P'
        elif(scoress>=40): return 'D'
        else: return 'T'


