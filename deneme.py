# fruits = ['apple', 'banana', 'cherry', 'cherry']

# x = fruits.count("cherry")
# print(x)
# fruits = ['apple', 'banana', 'cherry']

# cars = ['Ford', 'BMW', 'Volvo']

# fruits.extend(cars)
# print(fruits)
# fruits = ['apple', 'banana', 'cherry']

# x = fruits.index("cherry")
# print(x)

# string_1 = 'I quit smoking'

# new_list_1 = list(string_1)  # we created multi element list
# print(new_list_1)

# new_list_2 = [string_1]  # this is a single element list
# print(new_list_2)



# city = ["Ankara", "istanbul", "izmir" ]
# # pri+ity)

# new_city2 = [city]
# print(new_city2)

#new = 'I am a student'
# new1 = list(new)
# print(new1)
# new2 = [new]
# print(new2)

# warning = 'You must quit smoking!'

# print(len(list(warning)))
# print(list(warning))
# print(len(warning))

# empty_list_1= []
# print(empty_list_1)

# empty_list_2 = list()
# print(empty_list_2)
# empty_list_1.append('32, 33, 34')
# print(empty_list_1)


# list = ['2', '4', '5']
# list.insert(1, '3')
# print(list)
# list.remove(2)
# print(list)

# # my_list = [1, 3, 5, 7]
# # print(my_list * 3)

# txt = "Hello, welcome to my world."

# x = txt.index("e", 5, 10)

# print(x)

# txt = "Hello, welcome to my world."

# print(txt.find("q"))
# print(txt.index("q"))

# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist
# print(thislist)


# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']

# city_list = []
# city_list.append(city) # we have created a nested list

# print(city_list)

# odd_numbers = [[11, 13, 15], 17, 19, 21, 23, 25, 27, 29]

# print(odd_numbers[6])




# fruits = ['apple', 'banana', 'watermelon', 'orange', 'mango', 'avocado']

# fruit_list = []
# fruit_list.insert(0, fruits)
# print(fruit_list[0][2][7])


# count = list(range(11))
# print(count)

# print(count[0:7])

# print(len([[12, 34, 56]]))
# print(len([[12, 34, 56]][0]))

# print(([12, 34, 56][0]))


# list = "elma", "armut", "havuç"
# print(type(list))

# empty_tuple_1 = tuple()

# print(empty_tuple_1)
# print(type(empty_tuple_1))


# my_tuple=(1, 4, 3, 4, 5, 6, 7, 4)

# my_list = list(my_tuple)

# print(type(my_list), my_list)

# mountain = tuple('Alps')
# print(type(mountain), mountain)

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(5)

# print(x)

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(8)

# print(x)


# mix_value = (10, False, 'fruit', 1.618)
# mix_value.append(['vegetable', 2+3j])



# my_list = []
# my_list.range(:11)
# print(my_list)
# x = range(0, 11)

# print(x)

# range(11)
# print()

import numbers


# numbers = []
# numbers.range[11]
# # numbers.reverse()
# # numbers.sort()
# print(numbers)    

# grocer = ["banana", ["orange", 
#                     ["apple", "eggplant", "melon", "spinach", "cheese", "leek" ], 
#            "water"], 
#            "mandarin"]
# print(grocer[1][1][1::2])

# flowers = ["jasmine", "lavender", "rose", "tulip"]
# colors = ["red", "blue", "yellow", "green", "pink"]
# print("My two favorite {flowers} are tulip and rose, two favorite are blue and green.".format(flowers))



city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
index1 = city.pop(2)
print(city)
print(index1)