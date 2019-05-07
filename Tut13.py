from struct import * # Stores as bytes of data (0101...etc)
packed_data = pack('iif', 6, 19, 4.73)  #Format , values
print(packed_data)
print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))
#To get Data back to normal
orginal_data = unpack('iif', packed_data)
print(orginal_data)

income = [10, 30, 75]
def double_money(dollars):
    return dollars*2
new_income=list(map(double_money, income)) # The map will loop the list values through the function
print(new_income)