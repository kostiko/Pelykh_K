number=input("Input number of 4th digits: ")
print("Your number is  {}  ".format(number))
number=int (number)
sum1=number%10
number=number//10
sum2=number%10
number=number//10
sum3=number%10
number=number//10
sum4=number%10
#print (sum1,sum2,sum3,sum4)
print("Sum of digits is {}".format(sum1+sum2+sum3+sum4))

digits=input("Input number of 4th digits: ")
print("Your number is  {}  ".format(digits))
digits.split()

print("Sorted number is {}".format(''.join(sorted(digits))))