a=input("Input a: ")
b=input("Input b: ")
print("Before a={} b={}".format(a,b))
a,b=b,a
print("After changing a={} b={}".format(a,b))