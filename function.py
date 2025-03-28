def add():
    """This is demo"""
    print("This is sum function")
    list1 = [100, 10, 20, 30]
    sum1 = 0

    for num in list1:
        sum1 = sum1 + num
    return sum1


print("The sum of numbers in list : ", add())
