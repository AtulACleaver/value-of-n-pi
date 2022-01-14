import math


def value_of_pie(length):
    pi = round(math.pi, length)
    print(pi)


n = int(input("To what number do you want the value of pi: "))

value_of_pie(n)
