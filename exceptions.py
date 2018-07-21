try:
  x = int(input("Please enter a number: "))
  #break
except ZeroDivisionError:
  pass
except ValueError:
  print("Oops!  That was no valid number.  Try again...")
