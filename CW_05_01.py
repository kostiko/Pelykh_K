# def my_sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
#     print("After operator the return ")

# suma = my_sum(10, 20)
# print("Outside the function : ", suma)

# def my_print(str):
#     print(str)

# temp = my_print("first call function!")
# print(temp)



# def greet(name):
#     """This function greets to the person"""
#     print("Hello, " + name + ". Good morning!")
# print(greet.__doc__)

# def print_info(name, age):
#     print("Name: ", name)
#     print("Age: ", age)

# print_info(age=30, name="Alex")
# print("-" * 10)
# print_info(30, "Alex")

# def print_numbers(arg, *args):
#     print("arg: ")
#     print(arg)
#     print("args: ")
#     for var in args:
#         print(var)

# print_numbers(10)
# print("-" * 10)
# print_numbers(70, 60, 50, 40)

# def calc_factorial(x):    
# 	if x == 1 or x==0:
# 	        return 1    
# 	else:
# 	        return x * calc_factorial(x-1)

# print(calc_factorial(6))

# double = lambda x: x * 2
# print(double(5))

# print((lambda x: x * 2)(5))


# def sayHello():                
#     print('Hello world!')      
                               
# # # # ###################################3
  
# sayHello() 
# sayHello()                          # викликаємо функцію
# t=sayHello 
# print(t)                         # викликаємо функцію знову

# ##
# def add(x, y):
#     return x + y
# # # ##
# print(add(1, 10))
# # # ##
# print(add('abc', 'def'))

# def newfunc(n):
#     def myfunc(x):
#         return x + n
#     return myfunc

# new = newfunc(100)
# print(new(200))
# ###
# def func():
#     pass
# # # #
# print(func())
# ###Якщо функція нічого 
# # не повертає, а саме 
# # не завершується словом
# #return, то функція повертає 
# #значення None
# ##
# #example function
# ############################
# def my_function(argument):
#     print(argument)
# #
# my_function("abracadabra")

# ###################################################
#Required arguments (обовязкові аргументи функції)
# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
 
# #Коректне використання функції

# print_max(3, 4)      #аргументи — літеральні константи
 
# #Некоректне використання функції

# print_max()
# print_max(3)
# print_max(12,7,3)
# 
# ####################
# #   
# x = 5
# y = 7
# print_max(x, y) #змінні як аргументи


# #Keyword argument (аргументи-ключові слова)
# def person(name, age):
#     print(name, "is", age, "years old")
# #
# def person(name, age=25):
#     print(name, "is", age, "years old")
# person(name="John", age=35)
# # #
# person(age=23, name="John")

# #Default argument аргументи задані по замовчуванню

# def space(planet_name, center="Star"):
#     print(planet_name, "is orbiting a", center)
# #
# space("Mars")
# #
# space("Mars", "Black Hole")
# ###########
# # Variable-length arguments аргумент довільної довжини
# def unknown(*args):
#     for argument in args:
#         print(argument)
 
# # # # # #  ################
# unknown("hello","world")
# unknown(1,2,3,4,5) 
# unknown()

# #########

# #Аргументи функції,
# #Типові значення аргументів
# #########
# def say(message, times = 1):
#     print(message * times)
# # # #
# say('Hello')
# # #
# say('World', 5)
# ########################
# def func(a, b=5, c=10):
#     print('a is', a, 'and b is', b, 'and c is', c)
# # 
# func(3, 7)

# func(25, c=24)
# #
# func(c=50, a=100)
# func(b=50, c=100)
# #
# ############################
# # c - необовязковий аргумент
# def func(a, b, c=2): 
#     return a + b + c
# ###
# func(1, 2)
# ####
# func(1, 2, 3)
# ###
# func(a=1, b=3)
# ##
# func(a=3, c=6) #b не визначений, Error
# ###########################################

# # def func(a, b=5) правильно

# func(a=5, b) #неправильно

# # Тільки ті параметри, які знаходяться 
# # в кінці списку параметрів можуть 
# # мати типові значення. 
# ##########################
# #довільна кількість неіменованих аргументів
# # args це кортеж
# def func(*args):
#      return args
# # #
# print(func(1, 2, 3, 'abc'))
# ###
# print(func())
# ##
# print(func(1))

# #довільна кількість іменованих аргументів
# #змінна kwargs це словник 
# def func(**kwargs):
#     return kwargs
# # # ###
# w=func(a=1, b=2, c=3)
# print(w)
# # # ###
# t=func()
# print(t)
# ##
# w=func(a='python')
# print(w)
# ###



# #Лямбда функція (анонімна функція)


# def f(x):
#     return x**2

# # ####
# print(f(3))
# ####

# g=lambda x: x**2  
# # # #
# print(g(3))
# # #
# print((lambda x: x**2)(3))
#######
# func =lambda x, y: x + y
# #####
# func(1, 2)
# ######
# func('a', 'b')
# ######
# print((lambda x, y: x + y)(1, 2))
# #####
# (lambda x, y: x + y)('a', 'b')
# #####
# #Лямбда функція не потребує return
# func = lambda *args: args
# ####
# print(func(1, 2, 3, 4))
# #######################################
# map
# ##################################
# #Списки можна обробляти lambda-функціями 
# # всередині інших функцій, наприклад 
# # таких функцій як map(), filter(), reduce(),


# #######Глобальна змінна

# # глобальна змінна age
# age = 44
 
# def info():
#     print(age) # Друкуєм глобальну змінну age
#  # створюєм локальну змінну age 
# def local_info():
#     age = 22  
#     print(age)

# info() 
# # print("###########")
# local_info() 
# # ######################

# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)

# func(x)
# print('x is still', x)

# #####
# оператор global
# глобальна змінна age
# age = 13
 
# функція яка змінює глобальну змінну
# def get_older():
#     global age
#     age += 1
 
# print(age) # надрукує 13
# get_older() # збільшуєм age на 1
# print(age) # надрукує 14
# #############################
# #####
# # оператор nonlocal
# #############################
# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
# # #
# c = counter()
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4
# --------------------------------------------------------

# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел. 
# def ser_arifm(*argc):
#     return print(sum(argc)/len(argc))
# ser_arifm(1,2,3,4)
# --------------------------------------------------------

# 2.  Написати функцію, яка повертає абсолютне значення числа
# def absolut_value(val):
#     if val<0:
#         return -val
#     else:
#         return val
# print(absolut_value(int(input("value:  "))))
# --------------------------------------------------------

# 3.  Написати функцію, яка знаходить максимальне число з двох чисел, 
#     а також в функції використати рядки документації DocStrings.
# def max_number(num_1,num_2):
#     """Function of max numder"""
#     return max(num_1,num_2)
# print(max_number.__doc__)
# print ("Max number is {}".format(max_number(int(input("Ins3ert first number:")),int(input("Insert second number:")))))
# --------------------------------------------------------


# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола 
#     (написати три функції для обчислення площі, і викликати їх в головній програмі 
#     в залежності від вибору користувача)



# 5.  Написати функцію, яка обчислює суму цифр введеного числа.
# 6.  Написати програму калькулятор, яка складається з наступних функцій: 
#     головної, яка пропонує вибрати дію та додаткових, які реалізовують вибрані дії, 
#     калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора, після виходу, 
#     користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!
# 7.  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.
# 8.  Написати програму, яка обчислює дискримінант квадратного рівняння і обчислює його корені