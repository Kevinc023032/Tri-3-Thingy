---
title: Data Structures Projects
layout: template
filename: Data-Structures-Projects
--- 

[Week 0](https://kevinc023032.github.io/Tri-3-Thingy/Data-Structures-Projects#Week-0-Code-Snippets), [Week 1](https://kevinc023032.github.io/Tri-3-Thingy/Data-Structures-Projects#Week-1-Code-Snippets), [Week 2 ](https://kevinc023032.github.io/Tri-3-Thingy/Data-Structures-Projects#Week-2-Code-Snippets)

# Replit Link
<iframe height="1000px" width="900px" src="https://replit.com/@KevinChen138/Tri-3-Thingy?lite=true#main.py"></iframe>

# Week 0 Code Snippets
### Python Menu w/ data structures 
```aidl
# menu.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
import loopy
import mathpy
import funcy
import patterns


# Main list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
    ["Stringy", "stringy.py"],
    ["Listy", "listy.py"],
    ["Loopy", loopy.main],
]

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Factors", mathpy.factors],
    ["GCD", mathpy.gcd],
    ["LCM", mathpy.lcm],
    ["Primes", mathpy.primes],
]

patterns_sub_menu = [
    ["Patterns", "patterns.py"],
    ["PreFuncy", "prefuncy.py"],
    ["Funcy", funcy.ship],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Math", submenu])
    menu_list.append(["Patterns", patterns_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)

def patterns_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, patterns_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
```

# Week 1 Code Snippets
### InfoDB Lists
```aidl
KVDb = []
# List with dictionary records placed in a list  
KVDb.append({  
               "FirstName": "Kevin",  
               "LastName": "Chen",  
               "DOB": "Febuary 25",  
               "Location": "San Diego",  
               "Personal Email": "sdkc0225@gmail.com",  
               "School Email": "kevinc55921@stu.powayusd.com",  
               "Coding_Languages":["Python","HTML", ]  
              })  
```

# Week 2 Code Snippets
``` #Select your own Math function. Write it in Imperative and OOP form. Some Math functions have been provided. Think about inputs and outputs to present to Teacher. It is preferred to have Test data, not input to illustrate code.

``` #Write Factorial function using classes, providing implementation of call.
  #-Print the final number
class Factorial:
    def __init__(self):
      self.fact = 2
    def __call__(self, n):
      for x in range(4, n+2):
        self.fact = self.fact * x;
      
      return self.fact

D_facto = Factorial()    # instantiate the class object and run __init__

n=int(input("enter a positive number:"))
print(D_facto(n))            # execute __call__ and print result

# Function to find the mean between 3 numbers
```def findMean(num1, num2, num3):
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
