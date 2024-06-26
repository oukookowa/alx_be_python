#Draws a square sides equal to the entered number and made of asterics
square_length = int(input("Enter the size of the pattern: "))
if square_length < 1:
    square_length = 1

i = 1
while i in range(1, square_length + 1):
    j = 1
    for j in range(1, square_length + 1):
        print("*", end="") 
        j += 1
    print()
    i += 1
