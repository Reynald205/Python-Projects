def beef():  # How you create a function.
    print("Functions are cool")
def coin2usd(btc):
    amount = btc * 527
    print(amount)
def allowed_age(my_age):
    g_age = (my_age/2)+7
    return g_age  # Returns the value of g_age so function will = this.
def get_gender(gender = "unknown"): # Gives a default value to the function
    if gender is "m":
        gender = "Male"
    elif gender is "f":
        gender = "Female"
    print(gender)
get_gender("m")
get_gender("f")
get_gender()
my_limit = allowed_age(30)
beef() # How you call a function
coin2usd(3.85)
print(my_limit,"is the lowest to date before getting creepy.")
