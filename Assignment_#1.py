#####Question #1


# This asks the user to enter in their first, middle, and last name. Then takes that input and assigns it to the
# variable fullName.
fullName = input("Please enter your first, middle, and last name: ")

# This separates the users input based on the spaces and assigns each input after the space to the variable nameList.
nameList = fullName.split()

# These lines of code assigns the firstName, middleName, and lastName variables based on the spaces split from nameList.
firstName = nameList[0][0]
middleName = nameList[1][0]
lastName = nameList[2][0]

# This line of code outputs the first initial, middle initial and the last initial.
print("First, middle and last initials: " + firstName.upper(),".", middleName.upper(),".", lastName.upper(),".")


#####Question #2


#This line of code creates the variable investments. Then it assigns the variable investments to an empty list.
investments = []

#This line of code asks the user to enter amount invested in SPY. Then it passes the users input as float and assigns
#it to the variable investment.
investment = float(input("Enter amount invested in SPY: "))
#This line of code takes the variable invesment and appendes it to the investments list.
investments.append(investment)

#This line of code asks the user to enter amount invested in QQQ. Then it passes the users input as float and assigns
#it to the variable investment.
investment = float(input("Enter amount invested in QQQ: "))
#This line of code takes the variable invesment and appendes it to the investments list.
investments.append(investment)

#This line of code asks the user to enter amount invested in EEM. Then it passes the users input as float and assigns
#it to the variable investment.
investment = float(input("Enter amount invested in EEM: "))
#This line of code takes the variable invesment and appendes it to the investments list.
investments.append(investment)

#This line of code asks the user to enter amount invested in VXX. Then it passes the users input as float and assigns
#it to the variable investment.
investment = float(input("Enter amount invested in VXX: "))
#This line of code takes the variable invesment and appendes it to the investments list.
investments.append(investment)

#This line of code takes the sum of the numbers in the list investments and assigns it to the variable totalInvestments.
totalInvestments = sum(investments)

#This line of code takes the first number in the list investments and divides that number by the totalInvestments
# variable. Then assigns that number to the spyInvestment variable.
spyInvestment = (investments[0]) / (totalInvestments)

#This line of code takes the second number in the list investments and divides that number by the totalInvestments
# variable. Then assigns that number to the qqqInvestment variable.
qqqInvestment = (investments[1]) / (totalInvestments)

#This line of code takes the third number in the list investments and divides that number by the totalInvestments
# variable. Then assigns that number to the eemInvestment variable.
eemInvestment = (investments[2]) / (totalInvestments)

#This line of code takes the fourth number in the list investments and divides that number by the totalInvestments
# variable. Then assigns that number to the vxxInvestment variable.
vxxInvestment = (investments[3]) / (totalInvestments)

#This line of code outputs ETF the puts 2 tabs then outputs PERCENTAGE then goes to a new line to outputs
# ---------------------.
print("\nETF\t\tPERCENTAGE\n---------------------")

#This line of code outputs SPY then has a tab then outputs the spyInvestment variable. When outputing the spyInvestment
# variable it rounds it to have only 2 decimal places and have a % symbol at the end.
print("SPY\t{0:10.2%}".format(spyInvestment))

#This line of code outputs SPY then has a tab then outputs the qqqInvestment variable. When outputing the qqqInvestment
# variable it rounds it to have only 2 decimal places and have a % symbol at the end.
print("QQQ\t{0:10.2%}".format(qqqInvestment))

#This line of code outputs SPY then has a tab then outputs the eemInvestment variable. When outputing the eemInvestment
# variable it rounds it to have only 2 decimal places and have a % symbol at the end.
print("EEM\t{0:10.2%}".format(eemInvestment))

#This line of code outputs SPY then has a tab then outputs the vxxInvestment variable. When outputing the vxxInvestment
# variable it rounds it to have only 2 decimal places and have a % symbol at the end.
print("VXX\t{0:10.2%}".format(vxxInvestment))

#This line of code outputs TOTAL AMOUNT INVESTED: then outputs the totalInvestments variable, formating it to round the
# variable to only 2 decimal places and to have commas and to have a $ infront of the number.
print ("\nTOTAL AMOUNT INVESTED: ${0:10,.2f}".format(totalInvestments))


#####Question #3


#This line of code creates the variable numbers. Then it assigns the variable numbers to an empty list.
numbers = []

#This line of code asks the user to Enter the 1st number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 1st number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 2nd number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 2nd number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 3rd number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 3rd number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 4th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 4th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 5th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 5th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 6th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 6th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 7th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 7th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 8th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 8th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 9th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 9th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code asks the user to Enter the 10th number: . Then it passes the users input as float and assigns
#it to the variable num.
num = float(input("Enter the 10th number: "))
#This line of code takes the variable num and appendes it to the numbers list.
numbers.append(num)

#This line of code takes the minimum number from the numbers list and assigns it to the variable minimumNumber.
minimumNumber = min(numbers)

#This line of code takes the maximum number from the numbers list and assigns it to the variable maximumNumber.
maximumNumber = max(numbers)

#This line of code takes the sum of the numbers in the list numbers and assigns it to the variable totalNumbers.
totalNumbers = sum(numbers)

#This line of code takes the sum of the numbers in the list numbers and divides it by the length of the list, and then
# assigns that number to the variable average.
average = sum(numbers) / len(numbers)

#This line of code outputs The lowest number in the list is: then outputs the minimumNumber variable, formating it
# to round to only 2 decimal places.
print("\nThe lowest number in the list is: {0:.2f}".format(minimumNumber))

#This line of code outputs The highest number in the list is: then outputs the maximumNumber variable, formating it
# to round to only 2 decimal places.
print("The highest number in the list is: {0:.2f}".format(maximumNumber))

#This line of code outputs The total of the numbers in the list is: then outputs the totalNumbers variable,
# formating it to round to only 2 decimal places.
print("The total of the numbers in the list is: {0:.2f}".format(totalNumbers))

#This line of code outputs The average of the numbers in the list is: then outputs the average variable,
# formating it to round to only 2 decimal places.
print("The average of the numbers in the list is: {0:.2f}".format(average))