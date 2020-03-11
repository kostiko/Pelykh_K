# # 1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне,
# #  чи введені дані коректні.
try:
    num=int(input("Enter your number:")) 
    if num<=0:
        raise IOError("Number <=0")
    if num%2==0:
        print("Number is event")
    else:
        print("Number is not event")
    
# # note that braces () are necessary here for multiple exceptions 
# except NameError as e: 
# 	print(e)
# except ValueError: 
# 	print("ValueeeError")
# except TypeError as k:
#     print (k)
# except IOError as s:
#     print(s)

#---------------------------------------------------------------------------------
# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить 
# повідомлення про те чи вік є парним чи непарним числом. Необхідно передбачити можливість 
# введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію.
#  Головний код має викликати функцію, яка обробляє введену інформацію.


#---------------------------------------------------------------------------------
# 3. Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, 
# передбачити випадок ділення на нуль, 
# випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.
# try:


# try:
#     num_1=int(input("Enter first number: "))
#     num_2=int(input("Enter second number: "))
#     print ("Quotient is {}".format(num_1/num_2))

# except ZeroDivisionError as z:
#     print(z)
# except ValueError as v:
#     print(v)
# except TypeError as t:
#     print(t)
# else:
#     print ("Else")
# finally:
#     print("The END")


#---------------------------------------------------------------------------------
#  4. Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, 
#  який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
#  Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.
# days={1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday" }
# print (input("Enter number day of the week {}".format(days[])