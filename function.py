def add():

    print("This is sum function")
    list1 = [100, 10, 20, 30]
    sum = 0

    for num in list1:
        sum = sum + num
    return sum


print("The sum of numbers in list : ", add())
