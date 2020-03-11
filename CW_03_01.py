# start = 0
# finish = 10
# while start < finish:
#     print(start)
#     start += 1
# else:
#     print ("The end")

# for j in [0, 1, 2, 3, 4]:
#     print(j)
# else:
#     print(j, '- is the last')

# x=range(10)
# print(x)
# #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(range(5,10))
# #
# # [5, 6, 7, 8, 9]
# print(range(0,10,2))
# #[0, 2, 4, 6, 8]

# for val in "string":
#     if val == "i":
#         break
#     print(val)
# print("The end")

# for val in "string":
#     if val == "i":
#         continue    
#     print(val)
# print("The end")

#while


# i = 5
# while i < 15:
#     print(i)
#     i = i + 2

###################
#for

# for i in 'hello world':
#     # print(i * 2,end='№')
#     print(i * 2)


#у вище вказаному прикладі функція print() має 
# також аргумент end — він вказує, яким символом 
# має закінчуватись поточне виведення на екран. 
# Якщо в функції print() не вказаний даний аргумент 
# то виведення закінчується символом переходу на 
# нову стрічку (\n).
#for
#
# spisok = [10, 40, 20, 30]
# for element in spisok:
#     print(element + 2)
# print(spisok)
# ##for

# spisok = [10, 40, 20, 30]
# i = 0
# for element in spisok:
#      spisok[i] = element + 2
#      i += 1
#      print(element)
# print(spisok)


######################
#for для dictionary
######################

# d = {1:'one',2:'two',3:'three',4:'four'}
# for key in d:
#     d[key] = d[key] + '!'
# print(d)

##############
###while
#################
# 
# spisok = [10, 40, 20, 30]
# i = 0
# while i < len(spisok):
#     spisok[i] = spisok[i] + 2 
#     i=i + 1
# print(spisok)

# ##############################
# # continue виходить з ітерації, починає наступну
# ################################################

# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i * 2, end='')

###############################
#break достроково перериває цикл
#####################################

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end='')
    
    #Службове слово else, яке застосовується 
    # в циклі while чи for перевіряє чи був вихід 
    # з циклу з допомогою слова break, блок коду
    # після else буде виконаний лише у випадку 
    # якщо не спрацював break
    ############################### 
# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print('Букви a в стрічці нема')
# print("OOps!!!")
#range
##############################
# a = range(-10, 10)
# print(type(a))
# print(list(a))
# print(a)
# ####################

# spisok = [10, 40, 20, 30]
# print(list(range(len(spisok))))
# print(range(len(spisok)))

# range(0, 4) #генерує послідовність від 0 до 3
# spisok = [10, 40, 20, 30]
# for i in range(len(spisok)):
#     spisok[i] += 2
#     print(i,spisok[i])


# a=int(input("Input 1st number: "))
# b=int(input("Input 2nd number: "))
# if a>b:
#     print("{}>{}".format(a,b))
# else:
#    print("{}<{}".format(a,b))

# if a%2==0:
#    print ("{} parne".format(a))
# else:
#    print ("{} neparne".format(a))


# a=0
# while a<100:
#     print (a,end=' ')
#     a+=2


# for j in range(0,100,2):
#     print (j,end=' ')

#while a<100:
    #if a%2==0:
        #print (a,end=' ')
    
#for i in range(100):
        #print (i,end=' ')
        #if (i%2==0):
            #continue
        #print (i,end=' ')


# for i in range(1,100,1):
#             #print (i,end=' ')
#         if (i%2==0):
#             break
#         print (i,end=' ')

# for i in range(1,100,1):
#         i=float(i)
            
#         print (i,end=' ')

# n=int(input())
# sum=1

# for i in range(1,n+1):
#             #print (i,end=' ')
#         # if (i%2==0):
#         #     break
#          i*=i
# print (i,end=' ')
# a=list(range(5))
a=int(input('Enter digit: '))
sum=1
for i in (range(1,a+1)):
    (sum)=sum*i
    
print ('Factorial {}= {}'.format(i,sum))