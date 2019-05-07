class Parent:
    def last_name(self):
        print("Walme")


class Child(Parent):  #Inherits Parent
    def first_name(self):
        print("Reynald")

    #def last_name(self):  # Override the Parent
        #print("Victory")

panther = Child()
panther.first_name()
panther.last_name()