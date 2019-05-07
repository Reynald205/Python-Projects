def sentence(name="Rei",action="ate",item="burger"):
    print(name,action,item)
sentence()
sentence("Sally","shows","flowers")
sentence(action="fights",item="cancer") # Alternate way of entering arguments
print("=========================")
if __name__ == '__main__':
    def addnum(*args): # Makes the function take a flexible amount of arguments
        total = 0
        for a in args:
            total += a
        print(total)
addnum(5)
addnum(6,5)
addnum(5,6,9)
Sampledata =[27,20,0]
def healthcalc(age,num_apples,cigs_smoked):
    answer = (100-age)+(num_apples*3.5)-(cigs_smoked*2)
    print(answer)
healthcalc(Sampledata[0],Sampledata[1],Sampledata[2])
healthcalc(*Sampledata) # Unpacking an argument list