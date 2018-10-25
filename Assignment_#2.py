########################################################################################################Question 1 Code:

# #doc later
# #Variables
# lowLimit = 2
# midLimit = 6
# highLimit = 10
#
# #doc later
# packageWeight = eval(input("Enter the weight of the package: "))
#
# #doc later
# if (packageWeight >= highLimit):
#     #doc later
#     shippingRate = 4.75
#
# #doc later
# elif (packageWeight < highLimit and packageWeight >= midLimit):
#     #doc later
#     shippingRate = 4
#
# #doc later
# elif (packageWeight < midLimit and packageWeight >= lowLimit):
#     #doc later
#     shippingRate = 3
#
# #doc later
# elif (packageWeight < lowLimit):
#     #doc later
#     shippingRate = 1.5
#
# #doc later
# print("Shipping charge: ${0:4,.2f}".format(shippingRate))



########################################################################################################Question 2 Code:

#This is the main function
def main():

    # doc later
    scoresList = []

    # doc later
    letterGrades = []

    #doc later
    for scoreNumber in range(1, 6):
        #doc later
        score = float(input("Enter score {0:.0f}: ".format(scoreNumber)))
        #doc later
        scoresList.append(score)

    # doc later
    determine_grade(scoresList, letterGrades)

    # doc later
    firstScore = scoresList[0]
    secondScore = scoresList[1]
    thirdScore = scoresList[2]
    fourthScore = scoresList[3]
    fifthScore = scoresList[4]

    # doc later
    firstGrade = letterGrades[0]
    secondGrade = letterGrades[1]
    thirdGrade = letterGrades[2]
    fourthGrade = letterGrades[3]
    fifthGrade = letterGrades[4]

    # doc later
    print("\nScore\t Numeric Grade\t Letter Grade")

    #This outputs a simple ascii design
    ascii()

    #doc later
    print("Score 1:\t", firstScore, "\t", firstGrade)

    # doc later
    print("Score 2:\t", secondScore, "\t", secondGrade)

    # doc later
    print("Score 3:\t", thirdScore, "\t", thirdGrade)

    # doc later
    print("Score 4:\t", fourthScore, "\t", fourthGrade)

    # doc later
    print("Score 5:\t", fifthScore, "\t", fifthGrade)

    # This outputs a simple ascii design
    ascii()

#doc later
def determine_grade(scoresList, letterGrades):

    #doc later
    aGradeMaximum = 100
    aGradeMinimum = 90
    bGradeMaximum = 89.99
    bGradeMinimum = 80
    cGradeMaximum = 79.99
    cGradeMinimum = 70
    dGradeMaximum = 69.99
    dGradeMinimum = 60
    fGradeMaximum = 59.99
    fGradeMinimum = 0

    #doc later
    for score in scoresList:

        # doc later
        if (score >= aGradeMaximum or score >= aGradeMinimum):

            # doc later
            letterGrade = "A"
            #doc later
            letterGrades.append(letterGrade)

        # doc later
        elif (score <= bGradeMaximum and score >= bGradeMinimum):

            # doc later
            letterGrade = "B"
            # doc later
            letterGrades.append(letterGrade)

        # doc later
        elif (score <= cGradeMaximum and score >= cGradeMinimum):

            # doc later
            letterGrade = "C"
            # doc later
            letterGrades.append(letterGrade)

        # doc later
        elif (score <= dGradeMaximum and score >= dGradeMinimum):

            # doc later
            letterGrade = "D"
            # doc later
            letterGrades.append(letterGrade)

        # doc later
        elif (score <= fGradeMaximum and score >= fGradeMinimum):

            # doc later
            letterGrade = "F"
            #doc later
            letterGrades.append(letterGrade)


#This is some simple ascii design
def ascii():

    #This is some simple ascii design
    print("------------------------------------------------------------------")

#This calls the main function
main()

########################################################################################################Question 3 Code:
