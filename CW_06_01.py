# import pyowm

# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(input("Enter you city: "))
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

# #temp_max=w.get_temperature('celsius'[temp_max])
# print("Temperature current: {}".format(w.get_temperature('celsius')['temp']))
# print("Temperature max: {}".format(w.get_temperature('celsius')['temp_max']))
# print("Temperature min: {}".format(w.get_temperature('celsius')['temp_min']))
# print("Wind speed: {}".format(w.get_wind()['speed']))
# print("Humidity: {}".format(w.get_humidity()))

# import random
# gen_number=random.randint(1,100)
# print(gen_number)
# while True:
#     user_number=int(input("Enter your number"))
#     if user_number==gen_number:
#         print ("WOW!!!")
#         break
#     if user_number>gen_number:
#         print("Number <")
#     else:
#         print("Number>")

# 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисел від 1 до 100 і пропонує користувачу вгадати це число. Програма зчитує числа, які вводить користувач і видає користувачу підказки про те чи загадане число більше чи менше за введене користувачем. Гра має тривати до моменту поки користувач не введе число, яке загадане програмою, тоді друкує повідомлення привітання. 
#     (для виконання завдання необхідно імпортувати  модуль random, а з нього функцію randint())
# import random
# gen_number=random.randint(1,100)
# print(gen_number)
# while True:
#     user_number=int(input("Enter your number"))
#     if user_number==gen_number:
#         print ("WOW!!!")
#         break
#     if user_number>gen_number:
#         print("Number <")
#     else:
#         print("Number>")

# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2. 
#     (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
import math
def rectangle_area(length,width):
    return print("Rectangle area = {}".format(length*width))
def area_of_a_triangle(height,base):
    return print("Area of a triangle = {}".format(height/2*base))
def area_of_a_circle(radius):
    return print("Area of a circle = {}".format(math.pi*pow(radius,2)))

while True:
    choise=int(input("""If you want count area of rectangle - type'1'
                           triangle - type '2' 
                           circle - type '3'
                    Your choise: """))
    if choise==1:
        rectangle_area(int(input("Rectangle lenght: ")),int(input("Rectangle width: ")))
        break
    if choise==2:
        area_of_a_triangle(int(input("Triangle height: ")),int(input("Triangle base: ")))
        break
    if choise==3:
        area_of_a_circle(int(input("Circle radius: ")))
        break

        
