# #q1
# username = input("enter username")
# age = int(input("enter age"))
#
# print(f"Hello Mr.{username} aged {age}")
#
# #q2
# userinput = input("enter")
#
# try:
#     value = int(userinput)
# except ValueError:
#     try:
#         value = float(userinput)
#     except ValueError:
#         value = userinput
#
# #q3
# elements = ['apple', 'banana', 'kiwi']
# elements.append('orange')
# elements.remove('kiwi')
#
# for fruit in elements:
#     print(fruit.upper())
#
# #q4
# my_tuple = (1,2,3)
# first, second = my_tuple[:2]
# print(first)
# print(second)
#
# #q5
# students = {
# 'riaz': 'B+',
# 'ali': 'A+',
# 'kamal': 'B+',
# 'kela': 'B+',
# 'rafiq': 'C+'
# }
#
# print(students)

#q6
# list1 = []
# list2 = []
#
# for i in range(0,3,1):
#     element1 = int(input("Enter num for list 1 "))
#     element2 = int(input("Enter  for list 2"))
# list1.append(element1)
# list2.append(element2)
#
# set1 = set(list1)
# set2 = set(list2)
#
# print(f"union =  {set1 | set2}")
# print(f"intersection = {set1 & set2}")
# print(f"difference = {set1 - set2}")
#
# #q7
# num = input("Enter num\t")
# if num > 0:
#     print("Pos")
# elif num < 0:
#     print("Neg")
# else:
#     print("Zero")
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

#q8
# for i in range(1, 51, 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
#
#q9
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(4))
#
# #q10
# def is_prime(num):
#     if num <= 1:
#         return false
#     else:
#         for i in range(2, int(num ** 0.5), 1):
#             if i % num == 0:
#                 return false
#         return true
#
# num = int(input("enter num"))
# if is_prime(num):
#     print("prime")
# else:
#     print("Not prime")

#q11
# list4 = [2,4,6,8,10]
#
# print([i**2 for i in list4])
#
# #q12
# dict1 = {
#     'kela': 23,
#     'kamal': 23
# }
# dict2 = {
#     'lol': 76,
#     'kamal': 12
# }
#
# merged_dicts = {
#     **dict1, **dict2
# }
#
# print(merged_dicts)
#
# #q13
# list5 = [2,3,5,6,5,2]
# new_list = []
# for num in list5:
#     if num not in new_list:
#         new_list.append(num)
#
# print(new_list)

#q14
# def palindrome(line):
#     line = line.lower().replace(" ", "")
#
#     return line == line[::-1]
#
# print(palindrome('treert'))

#q15
# def fibonnaci(n):
#     sequence = [0, 1]
#     while len(sequence) < n:
#         sequence.append(sequence[-1] + sequence[-2])
#     return sequence[:n]
#
# user_inp = int(input("enter num\t"))
# print(fibonnaci(user_inp))
#
# #q16
# list9 = []
# for i in range(0,7,1):
#     element = int(input("Enter num\t"))
#
#     try:
#         list9.append(element)
#     except ValueError:
#         print("Error\n")
#
# average = 0.0
# sum = 0.0
# for num in list9:
#     sum += num
# average = sum/len(list9)
#
# print(average)

# #q17
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#
# #q18
# users = {}
#
# def register():
#     username = (input("Enter username\t"))
#     password = (input("Enter password\t"))
#
#     users[username] = password
#
# def login():
#     username = (input("Enter username\t"))
#     password = (input("Enter password\t"))
#
#     if username in users and password == users[username]:
#         print("lOGIN SUCCESSFUL")
#     else:
#         print("Incorrect creds")
#
# register()
# login()

#q19
# words = input("Entyer list of words").split()
# count = {}
#
# for word in words:
#     count[word] = count.get(word, 0) + 1
# print(count)

#q20
choice = input("convert to c or f")
if choice.lower() == 'c':
    f = float(input("enter temp in f"))
    c = (f - 32) * 5 / 9
    print("c = ", c)
elif choice.lower() == 'f':
    c = float(input("enter temp in c"))
    f = c * 9 / 5 + 32
    print("f = ", f)
else:
    print("invalid")

