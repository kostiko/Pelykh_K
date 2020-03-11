def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    if fuel_left>=(distance_to_pump/mpg):
        return 1
    else:
        return 0