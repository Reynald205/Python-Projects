import Tut3 #import other functions in other files
import random #Random is a module that was downloaded online
classmates = {'Tony':'He is cool','Emma':'Afraid of water','Jack':'Whines about his girl'}
#How Keywords are used to make a dictionary using {}
print(classmates)
print(classmates['Emma'])
for k,v in classmates.items():# Stands for Key:Value
    print(k,v)
print('My limit is age',Tut3.allowed_age(23))#How other functions are called Filename.function()
x = random.randrange(1,7)
print(x)