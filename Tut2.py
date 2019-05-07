# The way to add comments for one line
'''This is the way to comment on multiple lines.'''
magicnum = 26
print(9,"This a string ") # To combine numbers and string you must use ','.
for n in range(101):
    if n is magicnum:
        print(n,"is the magic number")
        break  #This ends the loop'''
    else:
        print(n)
print("=========================")
for n in range(0,101,4):
    print(n)
print("=========================")
numbers = [2, 5, 12, 13, 17]
print("Here are the numbers still available.")
for n in range(1,20):
    if n in numbers:
        continue #Causes the program to move on without changing anything.
    else:
        print("The number",n,"is still available.")