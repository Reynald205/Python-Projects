answer = lambda x: x*7  # Sub for function.
print(answer(5))

date, item, price = ['December 23, 1956', 'Boxing Gloves', 8.51] # Called unpacking a list.
first = ['Tom', 'Bob', 'Dave']
second = ['Hanks', 'Sagat', 'Chapelle']
names = zip(first, second)  # zip takes two list to combine into a new list
for a, b in names:
    print(a, b)


def Drop_first_and_last(grades):
    first, *middle, last = grades # With the star the middle combines all the things except first and last
    avg = sum(middle) / len(middle)
    print(avg)

Drop_first_and_last([55, 76, 88, 96, 86, 76])
Drop_first_and_last([55, 76, 88, 96, 86, 76, 78, 89, 90, 99, 100, 56])