# write a program that generates imaginary coordinates for a rectangle
# generate random x1
# generate random y1
# x2 = x1+5
# y2 = y1+10
import random
x1 = random.randint(0,10)
y1 = random.randint(0,10)
x2 = x1 + 5
y2 = y1 + 10

print(x1,y1,x2,y2)

x, y = input("Enter two values for the first rectangle point: ").split()
z, h = input("Enter two values for the first rectangle point: ").split()

x = int(x)
y = int(y)
z = int (z)
h = int (h)

if x < x1 or y < y1 or z > x2 or h > y2:
    print ("False")
else:
    print("True")


