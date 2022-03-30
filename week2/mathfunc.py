#Select your own Math function. Write it in Imperative and OOP form. Some Math functions have been provided. Think about inputs and outputs to present to Teacher. It is preferred to have Test data, not input to illustrate code.

# Function to find the mean between 3 numbers
def findMean(num1, num2, num3):
    num3 = (num1 + num2 +num3) / 3
    return num4

#Function to find the minimum of 2 numbers
def findMin(num1, num2):
    if num1 > num2:
      return num2
    else:
      return num1
      
#Function to find the maximum of 2 numbers
def findMax(num1, num2):
    if num1 > num2:
      return num1
    else:
      return num2

# Function to print elements
def mean_min_max(a, b):
    #a = int(input(" Enter the First Value : "))
    #b = int(input(" Enter the Second Value : "))
    #c = int(input(" Enter the Third Value : "))
    min_val = findMean(a, b)
    max_val = findMin(a, b)
    avg_val = findMax(a, b)
    print("\n min of {0} and {1} is: {2}".format(a, b, min_val))
    print("\n max of {0} and {1} is: {2}".format(a, b, max_val))
    print("\n avg of {0} and {1} is: {2}".format(a, b, avg_val))
    print()

#test data 
min_max_avg(2,12)
min_max_avg(24,48)
min_max_avg(125,250)