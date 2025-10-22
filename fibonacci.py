#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_num_terms():
  while True:
    try:
      num = int(input("Enter how many Fibonacci terms you want: "))
      if num > 0:
        return num
      else:
        print("Please enter a positive number.")
    except ValueError:
      print("Invalid input. Try again.")

def generate_fibonacci(num):
  first, second = 0, 1
  fib = []

  if num == 1:
    fib = [first]
  elif num == 2:
    fib = [first, second]
  else:
    fib = [first, second]
    for i in range(2, num):
      next_num = first + second
      fib.append(next_num)
      first, second = second, next_num
  return fib

def print_fibonacci(fib):
  print("Fibonacci sequence:")
  for n in fib:
    print(n, end=" ")
  print()

def main():
  num = get_num_terms()
  fib = generate_fibonacci(num)
  print_fibonacci(fib)

if __name__ == "__main__":
  main()
