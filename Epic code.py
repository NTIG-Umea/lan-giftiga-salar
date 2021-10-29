import random
import time
b = True
while b:
  a = ""
  for y in range(6):
    x = ["n", "t", "i", "l", "a", "n"]
    a = a +  random.choice(x)
  print (a)
  b = "ntilan" != a