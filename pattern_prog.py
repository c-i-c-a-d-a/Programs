#Printing a Z and a reverse-Z pattern in python
("Pattern 1:")
for i in range (0,7):
    for j in range(0,7):
        if i==0 or i==6:
            print("#",end="")
        elif i==j:
            print("#",end="")
        else:
            print(" ",end="")
    print()
print("Pattern 2:")
for i in range (0,7):
    for j in range(0,7):
        if i==0 or i==6:
            print("#",end="")
        elif i+j==6:
            print("#",end="")
        else:
            print(" ",end="")
    print()
