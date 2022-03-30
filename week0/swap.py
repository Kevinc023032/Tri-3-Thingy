# helper swap function that swaps based on input
def swap():
  x = int(input('Whats your first number?:'))
  y = int(input('Whats your second number?:'))
  x,y = swap1(x,y)
  print(x,y) 

# actual algorithm/code for the swap
def swap1(a,b):
  if a > b:
    b, a = a, b  # swap values
  else:
    a, b = a, b
  return a, b  # return 2 values