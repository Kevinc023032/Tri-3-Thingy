# factorial_class.py

class Factorial:
    def __init__(self):
        self.factorialSeq = [1,1]

  #__call__ is a special function in Python that, when implemented inside a class,
    # gives its instances (objects) the ability to behave like a function.
    # It means after implementing __call__ method inside the Python class,
    # we can invoke its instances like a function
    def __call__(self, n):
        if n < len(self.factorialSeq):
            return self.factorialSeq[n]
        else:
            # Compute the requested Factorial number
            factorial_number = n * self(n - 1)
            self.factorialSeq.append(factorial_number)
        return self.factorialSeq[n]

factor_of = Factorial() # object instantiation and run __init__ method
print(factor_of(7)) # object running __call__ method

def tester():
    # Make a factorial object
    while True:
        factorial_of = Factorial()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            #The isinstance() function in Python returns true or false if a variable matches a
            # specified data type. isinstance(variable_to_check, data_type)
            if not (isinstance(n, int) and n >= 0):
                raise ValueError
            print("{0}! is: ".format(n))
            print(factorial_of(n)) # print the nth term
            break
        except:
            print(f'Poopy input, got "{n}" Try again.')

if __name__ == "__main__":
    tester()