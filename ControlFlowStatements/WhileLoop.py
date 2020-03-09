# while statement can be used with else in python

x = 0
while x < 5:
    print(x)
    x += 1
else:
    print("x is not equal to 5")

# break, continue, pass
# pass - do nothing at all
x=0
while x < 10:
    if x == 9:
        print("Printing")
        break
    print(x)
    x += 1
print("Out of loop now")