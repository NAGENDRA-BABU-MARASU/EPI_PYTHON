def check_if_power_of_two(x):
    return (str(int(x)) + " is a power of 2 :" + str(x & ( x -1) == 0))


print(check_if_power_of_two(0b1000))
print(check_if_power_of_two(0b1001))