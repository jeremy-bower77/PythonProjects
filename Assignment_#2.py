########################################################################################################Question 1 Code:

# These are the variables that are used for the if elif statements for assigning the shipping rate
noWeight = 0
lowLimit = 2
midLimit = 6
highLimit = 10

# This asks the user to enter in the weight of the package and assigns it to the variable packageWeight.
packageWeight = eval(input("Enter the weight of the package: "))

# This is an if statement that checks to see if the packageWeight is below the highLimit
if (packageWeight >= highLimit):
    # If this if statement is true then it assigns the shippingRate to 4.75
    shippingRate = 4.75

# This is an elif statement that checks to see if packageWeight is < highLimit and is >=midLimit
elif (packageWeight < highLimit and packageWeight >= midLimit):
    # If this elif statement is true then it assigns the shippingRate to 4
    shippingRate = 4

# This is an elif statement that checks to see if packageWeight is < midLimit and is >=lowLimit
elif (packageWeight < midLimit and packageWeight >= lowLimit):
    # If this elif statement is true then it assigns the shippingRate to 3
    shippingRate = 3

# This is an elif statement that checks to see if packageWeight is < lowLimit and is > noWeight
elif (packageWeight < lowLimit and packageWeight > noWeight):
    # If this elif statement is true then it assigns the shippingRate to 3
    shippingRate = 1.5

# This is an else statement. This will run if the other if and elif statements are not true.
else:
    # If this elif statement is true then it assigns the shippingRate to 0.0, and it will ask the user to re-enter the
    # packageWeight.
    shippingRate = 0.0
    print("The package weight that you entered was incorrect.\nPlease reenter the package weight.")

# This outputs the shippingRate based on the packageWeight that the user entered
print("Shipping charge: ${0:4,.2f}".format(shippingRate))



#######################################################################################################Question 2 Code:

# This is the main function
def main():

    # This is the score list
    scoresList = []

    # This is the score list
    letterGrades = []

    # This is a for loop that keeps looping the scoreNumber from 1 to 5 until there are 5 scores that are entered
    for scoreNumber in range(1, 6):
        # This asks the user to enter in a score and it takes the users input and assigns it to the variable score
        score = float(input("Enter score {0:.0f}: ".format(scoreNumber)))
        # This takes the variable score and appends it to the scoresList
        scoresList.append(score)

    # This is calling the calc_average function and is passing the scoresList to it
    calc_average(scoresList)

    # This is calling the determine_grade function and is passing the scoresList and the letterGrades to it
    determine_grade(scoresList, letterGrades)

    # This displays a simple table header starting with Score then Numeric Grade and last Letter Grade
    print("Score\t\t Numeric Grade\t Letter Grade")

    # This outputs a simple ascii design
    ascii()

    # This line of code outputs the first score from the scoresList and outputs the first grade from the letterGrades
    # that was assigned for the first score.
    print("Score 1: {0:10,.1f}".format(scoresList[0]), "\t\t", letterGrades[0])

    # This line of code outputs the second score from the scoresList and outputs the second grade from the letterGrades
    # that was assigned for the second score.
    print("Score 2: {0:10,.1f}".format(scoresList[1]), "\t\t", letterGrades[1])

    # This line of code outputs the third score from the scoresList and outputs the third grade from the letterGrades
    # that was assigned for the third score.
    print("Score 3: {0:10,.1f}".format(scoresList[2]), "\t\t", letterGrades[2])

    # This line of code outputs the fourth score from the scoresList and outputs the fourth grade from the letterGrades
    # that was assigned for the fourth score.
    print("Score 4: {0:10,.1f}".format(scoresList[3]), "\t\t", letterGrades[3])

    # This line of code outputs the fifth score from the scoresList and outputs the fifth grade from the letterGrades
    # that was assigned for the fifth score.
    print("Score 5: {0:10,.1f}".format(scoresList[4]), "\t\t", letterGrades[4])

    # This outputs a simple ascii design
    ascii()

    # This line of code outputs the average score for the scoresList and outputs the grade from the letterGrades
    # that the average score has.
    print("Average score: {0:2,f}".format(scoresList[5]), "\t", letterGrades[5])


# This is the calc_average that calls the scoresList from the main and calculates the average of the scores
def calc_average(scoresList):

    # This formula calculates the average score from the scores list
    score = sum(scoresList) / len(scoresList)
    # This appends the average score to the scoresList
    scoresList.append(score)


# This is the determine_grade that calls the scoresList and letterGrades list from the main and assigns a letter grade
# for each of the scores entered.
def determine_grade(scoresList, letterGrades):

    # These are the variables that are used for the if elif statements for assigning the letter grades to the scores
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

    # This is a for loop that loops for each score in the scoresList
    for score in scoresList:

        # This is an if statement that checks to see if the score higher or equal to the aGradeMaximum or if the score
        # higher or equal to the aGradeMinimum.
        if (score >= aGradeMaximum or score >= aGradeMinimum):

            # This assigns the letterGrade to A
            letterGrade = "A"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)

        # This is an elif statement that checks to see if the score lower or equal to the bGradeMaximum and if the score
        # higher or equal to the bGradeMinimum.
        elif (score <= bGradeMaximum and score >= bGradeMinimum):

            # This assigns the letterGrade to B
            letterGrade = "B"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)

        # This is an elif statement that checks to see if the score lower or equal to the cGradeMaximum and if the score
        # higher or equal to the cGradeMinimum.
        elif (score <= cGradeMaximum and score >= cGradeMinimum):

            # This assigns the letterGrade to C
            letterGrade = "C"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)

        # This is an elif statement that checks to see if the score lower or equal to the dGradeMaximum and if the score
        # higher or equal to the dGradeMinimum.
        elif (score <= dGradeMaximum and score >= dGradeMinimum):

            # This assigns the letterGrade to D
            letterGrade = "D"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)

        # This is an elif statement that checks to see if the score lower or equal to the fGradeMaximum and if the score
        # higher or equal to the fGradeMinimum.
        elif (score <= fGradeMaximum and score >= fGradeMinimum):

            # This assigns the letterGrade to F
            letterGrade = "F"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)

        # This is an else statement that runs if the none of the other if and elif statements are true.
        else:

            # This assigns the letterGrade to E
            letterGrade = "E"
            # This appends the letterGrade to the letterGrades list
            letterGrades.append(letterGrade)



#This is some simple ascii design
def ascii():

    #This is some simple ascii design
    print("-------------------------------------------------")

#This calls the main function
main()

#######################################################################################################Question 3 Code:

# This is the main function
def main():

    # This assigns reads the Q4-Data.txt file and assigns it to the originalList variable
    originalList = open("Q4-Data.txt", 'r')

    # This calls the list_sorted function and passing the originalList. Then it is assigned to the variable ogList.
    ogList = text_read(originalList)

    # This closes the originalList file
    originalList.close()

    # This outputs the header Original List: and then calls the ascii function. Followed by outputting the ogList.
    print("Original List:")
    ascii()
    print(ogList)

    # This calls the list_sorted function and passing the ogList. Then it is assigned to the variable sortedList.
    sortedList = list_sorted(ogList)

    # This outputs the header Sorted List: and then calls the ascii function. Followed by outputting the sortedList.
    print("\nSorted List:")
    ascii()
    print(sortedList)

    # This calls the new_list_create function and passing the sortedList. Then it is assigned to the variable
    # twoDimensionList.
    twoDimensionList = new_list_create(sortedList)

    # This outputs the header Two Dimension List: and then calls the ascii function. Followed by outputting the
    # twoDimensionList.
    print("\nTwo Dimension List:")
    ascii()
    print(twoDimensionList)

    # This calls the list_separate function and passing the twoDimensionList. Then it is assigned to the variables
    # nameList, codeList, salaryList.
    nameList, codeList, salaryList = list_separate(twoDimensionList)

    # This outputs the header List of Names: and then calls the ascii function. Followed by outputting the
    # nameList.
    print("\nList of Names:")
    ascii()
    print(nameList)

    # This outputs the header List of Codes: and then calls the ascii function. Followed by outputting the
    # codeList.
    print("\nList of Codes:")
    ascii()
    print(codeList)

    # This outputs the header List of Salaries: and then calls the ascii function. Followed by outputting the
    # salaryList.
    print("\nList of Salaries:")
    ascii()
    print(salaryList)


# This is the text_read that calls the originalList from the main.
def text_read(originalList):

    # This line of code assigns the originalList to the variable ogList
    ogList = ([line.rstrip() for line in originalList])

    # This returns the ogList to the main
    return ogList


# This is the list_sorted that calls the ogList from the main.
def list_sorted(ogList):


    # This line of code sorts the ogList by the salary in assending order and assigns it to the variable sortedList
    sortedList = sorted(ogList, key=lambda line: line.split(" ")[3], reverse=False)

    # This returns the sortedList to the main
    return sortedList



# This is the new_list_create that calls the sortedList from the main.
def new_list_create(sortedList):

    # This takes each object in the sortedList and splits them apart and assigns it to the twoDimensionList variable
    twoDimensionList = [line.split(" ") for line in sortedList]

    # This returns the twoDimensionList to the main
    return twoDimensionList


# This is the list_separate that calls the twoDimensionList from the main.
def list_separate(twoDimensionList):


    # This assigns the first two elements in the twoDimensionList and assigns it to the nameList
    nameList = [' '.join(name[0:2])for name in twoDimensionList]

    # This assigns the third element in the twoDimensionList and assigns it to the codeList
    codeList = [' '.join(code[2:3]) for code in twoDimensionList]

    # This assigns the fourth element in the twoDimensionList and assigns it to the salaryList
    salaryList = [' '.join(salary[3:4]) for salary in twoDimensionList]

    # This returns nameList, codeList, salaryList to the main
    return nameList, codeList, salaryList


#This is some simple ascii design
def ascii():

    #This is some simple ascii design
    print("-----------------------------------------------------------------------------------------------------------")

# This calls the main function
main()
