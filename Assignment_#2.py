########################################################################################################Question 1 Code:

# #doc later
# #Variables
# noWeight = 0
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
# elif (packageWeight < lowLimit and packageWeight > noWeight):
#     #doc later
#     shippingRate = 1.5
#
# #doc later
# else:
#     #doc later
#     shippingRate = 0.0
#     print("The package weight that you entered was incorrect.\nPlease reenter the package weight.")
#
# #doc later
# print("Shipping charge: ${0:4,.2f}".format(shippingRate))



########################################################################################################Question 2 Code:

# #This is the main function
# def main():
#
#     #This is the score list
#     scoresList = []
#
#     # doc later
#     letterGrades = []
#
#     #doc later
#     for scoreNumber in range(1, 6):
#         #doc later
#         score = float(input("Enter score {0:.0f}: ".format(scoreNumber)))
#         #doc later
#         scoresList.append(score)
#
#     # doc later
#     calc_average(scoresList)
#
#     # doc later
#     determine_grade(scoresList, letterGrades)
#
#     # doc later
#     print("Score\t\t Numeric Grade\t Letter Grade")
#
#     #This outputs a simple ascii design
#     ascii()
#
#     #doc later
#     print("Score 1: {0:10,.1f}".format(scoresList[0]), "\t\t", letterGrades[0])
#
#     # doc later
#     print("Score 2: {0:10,.1f}".format(scoresList[1]), "\t\t", letterGrades[1])
#
#     # doc later
#     print("Score 3: {0:10,.1f}".format(scoresList[2]), "\t\t", letterGrades[2])
#
#     # doc later
#     print("Score 4: {0:10,.1f}".format(scoresList[3]), "\t\t", letterGrades[3])
#
#     # doc later
#     print("Score 5: {0:10,.1f}".format(scoresList[4]), "\t\t", letterGrades[4])
#
#     # This outputs a simple ascii design
#     ascii()
#
#     #doc later
#     print("Average score: {0:2,f}".format(scoresList[5]), "\t", letterGrades[5])
#
#
# #doc later
# def calc_average(scoresList):
#
#     # doc later
#     score = sum(scoresList) / len(scoresList)
#     #doc later
#     scoresList.append(score)
#
#
# #doc later
# def determine_grade(scoresList, letterGrades):
#
#     #doc later
#     aGradeMaximum = 100
#     aGradeMinimum = 90
#     bGradeMaximum = 89.99
#     bGradeMinimum = 80
#     cGradeMaximum = 79.99
#     cGradeMinimum = 70
#     dGradeMaximum = 69.99
#     dGradeMinimum = 60
#     fGradeMaximum = 59.99
#     fGradeMinimum = 0
#
#     #doc later
#     for score in scoresList:
#
#         # doc later
#         if (score >= aGradeMaximum or score >= aGradeMinimum):
#
#             # doc later
#             letterGrade = "A"
#             #doc later
#             letterGrades.append(letterGrade)
#
#         # doc later
#         elif (score <= bGradeMaximum and score >= bGradeMinimum):
#
#             # doc later
#             letterGrade = "B"
#             # doc later
#             letterGrades.append(letterGrade)
#
#         # doc later
#         elif (score <= cGradeMaximum and score >= cGradeMinimum):
#
#             # doc later
#             letterGrade = "C"
#             # doc later
#             letterGrades.append(letterGrade)
#
#         # doc later
#         elif (score <= dGradeMaximum and score >= dGradeMinimum):
#
#             # doc later
#             letterGrade = "D"
#             # doc later
#             letterGrades.append(letterGrade)
#
#         # doc later
#         elif (score <= fGradeMaximum and score >= fGradeMinimum):
#
#             # doc later
#             letterGrade = "F"
#             #doc later
#             letterGrades.append(letterGrade)
#
#         #doc later
#         else:
#
#             #doc later
#             letterGrade = "N/A"
#             #doc later
#             letterGrades.append(letterGrade)
#
#
#
# #This is some simple ascii design
# def ascii():
#
#     #This is some simple ascii design
#     print("-------------------------------------------------")
#
# #This calls the main function
# main()

########################################################################################################Question 3 Code:

#doc later
def main():

    #doc later
    originalList = open("Q4-Data.txt", 'r')


    print("Original List:")
    ascii()
    #doc later
    ogList = text_read(originalList)

    print("\nSorted List:")
    ascii()
    #doc later
    list_sorted(ogList)



#doc later
def text_read(originalList):

    #doc later
    ogList = ([line.rstrip() for line in originalList])
    originalList.close()
    print(ogList)
    return ogList


#doc later
def list_sorted(ogList):

    #This can sort and print out the names but doesn't quite help.
    ogList.sort(key=lambda line: line.split()[-1])
    nameString = ", ".join(ogList)
    print(nameString)

    # #Not sure what to do here
    # sortedList = sorted(ogList, key=lambda txt: txt[3])
    #
    # print(sortedList)



# #doc later
# def new_list_create():
#
#     #doc later

# #doc later
# def list_separate():
#
#     #doc later

#This is some simple ascii design
def ascii():

    #This is some simple ascii design
    print("-----------------------------------------------------------------------------------------------------------")

#doc later
main()
