# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []
# List with dictionary records placed in a list  
InfoDb.append({  
              "FirstName": "Kevin",  
              "LastName": "Chen",   
              "DOB": "Febuary 25",  
              "Location": "San Diego",  
              "Personal Email": "sdkc0225@gmail.com",  
              "School Email": "kevinc55921@stu.powayusd.com",  
              "Coding_Languages":["Python","HTML", ]  
})  

InfoDb.append({  
              "FirstName": "Allyson",  
              "LastName": "Wong",   
              "DOB": "January 09",  
              "Location": "Houston",  
              "Personal Email": "aintnoway@gmail.com",  
              "School Email": "yourmom@stu.powayusd.com",  
              "Coding_Languages":["JS", "Python","HTML", ]
              })  


# given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["FirstName"],
          InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Coding Languages: ",
          end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(
        InfoDb[n]
        ["Coding_Languages"]))  # join allows printing a string list with separator
    print()


# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

# for loop iterates on length of InfoDb
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
    
def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion