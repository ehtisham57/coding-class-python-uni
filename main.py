# print("Hello Class");
# def addition(x):
#     return x*2
# print((addition(3)))

# add = lambda x:x*2
# print(add(3))

# cube = lambda x: x*x*x
# print(cube(3))

# avg = lambda x , y , z: (x+y+z) / 3
# print(avg(3,4,5))

# sort function in lambda

# def a_first(a):
#     return a[1]
# a=[[1,14],[5,8],[9,17]]
# a.sort(key=a_first)
# print(a)

# a=[[1,14],[5,8],[9,17]]
# a.sort(key=lambda x:x[1])
# print(a)

# a=[[1,14],[5,8],[9,17]]
# a.sort(key=lambda x:x[0])
# print(a)

#condition in lambda

# Max = lambda a, b : a if(a > b) else b
# print(Max(1, 2))

# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)

# import functools
# lis = [1, 3, 5, 2, 6, ]
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

# covert a lisit of integers in thier squares by using lambda

# numbers = [1,2,3,4,5,6,7]
# square = list(map(lambda x : x**2,numbers))
# print(square)

# sorted a list of string on alphabetical characters length 

# friuts = ['apple','banana', 'mango', 'cherry', 'date', 'elderberry']
# print(sorted(friuts))

# friuts = ['apple','banana', 'mango', 'cherry', 'date', 'elderberry']
# print(sorted(friuts, key=lambda x:len(x)))

# complex examples 

# people = [
#     {"name": "Alice", "age": 28, "city": "New York"},
#     {"name": "Bob", "age": 35, "city": "Los Angeles"},
#     {"name": "Charlie", "age": 22, "city": "Chicago"},
#     {"name": "David", "age": 31, "city": "Houston"},
#     {"name": "Eve", "age": 25, "city": "Miami"},
#     {"name": "Frank", "age": 30, "city": "Seattle"},
#     {"name": "Grace", "age": 27, "city": "Boston"},
#     {"name": "Hannah", "age": 29, "city": "San Francisco"},
#     {"name": "Isaac", "age": 33, "city": "Denver"},
#     {"name": "Jack", "age": 26, "city": "Austin"}
# ]

# print(sorted(people, key= lambda x : x['name']))