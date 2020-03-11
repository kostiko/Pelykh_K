# mylist = [True, True, True]
# # x = all(mylist)
# print(all(mylist))
# ###################
# mylist = [0,1,1]
# # x = all(mylist)
# print(any(mylist))
# ###################
# mydict = {0:"Apple",1:"Orange"}
# #x = all(mydict)
# print(all(mydict))

# x = ['apple','banana','cherry']
# # y = enumerate(x)
# print(list(enumerate(x)))

# pow2 = [2 ** x for x in range(10)]
# print(pow2)
# # Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

# odd = [x for x in range(20) if x % 2 == 1] 
# print (odd)
# # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19] 

# print([x+y for x in ['Python ','C '] for y in ['Language','Programming']]) 
#['Python Language', 'Python Programming', 'C Language', 'C Programming'] 

# for fruit in ['apple','banana','mango']:    
# 	print("I like",fruit)

# fruits = ("apple", "banana", "cherry")
# x = fruits.count("cherry")
# print(x)
# ######################
# fruits = (1, 4, 2, 9, 7, 8, 9, 3, 1)
# x = fruits.count(9)
# print(x)

# squares = {x: x*x for x in range(6)}
# print(squares)
# # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# d = {'name': 'Vasyl', 'surname': 'Bilan','id': '1', 'task': 'run application'}
# for key in d:
#     print("student {} = {}".format(key, d[key]))

# for key, val in d.items():
#     print("{} = {} .".format(key, val))
    
# for key in d.keys():
#     print("student {} = {}".format(key, d[key]))
    
# for val in d.values():
#     print("student {} = {}".format("?", val))





# digits=int(input("How much digits? "))
# m_list = [ int(input("Enter number")) for x in range(digits)]
# print(m_list)
# print("Min={}".format(min(m_list)))
# print("Max={}".format(max(m_list)))

# m_list = [ x for x in range(1,11) if x%2==0]
# print(m_list)
# m_list = [ x for x in range(1,11) if x%3==0]
# print(m_list)
# m_list = [ x for x in range(1,11) if x%2!=0 and x%3!=0]
# print(m_list)

# a=int(input('Enter digit: '))
# sum=1
# for i in (range(1,a+1)):
#     (sum)=sum*i

# print ('Factorial {} = {}'.format(i,sum))

# user_login=input("Login: ")
# while user_login=='First':
#     print("HI,First")
#     break
# else:
#     print("Error")

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     #Happy Coding! ;)
#     if fuel_left>=(distance_to_pump/mpg):
#         return 1
#     else:
#         return 0
    


