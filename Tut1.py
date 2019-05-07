print("I love tuna.")
age = 13
if age < 21:
    print("No beer for you!")

name = "Sammy"
if name is "Bucky":
    print("Hey there Bucky")
elif name is "Lucy":
    print("Hello Lucy")
else:
    print("Please sign into the site")

foods = ['bacon', 'tuna', 'ham', 'cheese', 'beef']
for f in foods[2:]:
    print(f)
    print(len(f))
print("=========================")
for x in range(5, 12, 2):
    print(x)
print("=========================")
butter = 5

while butter < 10:
    print(butter)
    butter += 1