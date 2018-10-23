########################################################################################################Question 1 Code:

#doc later
#Variables
lowLimit = 2
midLimit = 6
highLimit = 10

#doc later
packageWeight = eval(input("Enter the weight of the package: "))

#doc later
if packageWeight >= highLimit:
    #doc later
    shippingRate = 4.75

#doc later
elif packageWeight < highLimit and packageWeight >= midLimit:
    #doc later
    shippingRate = 4

#doc later
elif packageWeight < midLimit and packageWeight >= lowLimit:
    #doc later
    shippingRate = 3

#doc later
elif packageWeight < lowLimit:
    #doc later
    shippingRate = 1.5

#doc later
print("Shipping charge: ${0:4,.2f}".format(shippingRate))



########################################################################################################Question 2 Code:

########################################################################################################Question 3 Code:
