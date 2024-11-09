num = 0

num = int(input("Please enter an integer number between 1 and 100: "))


if (1 <= num <= 100):
    squ = num * num

    odd = 1
    square = 0
    series = "Square of Number " + str(num) + " = "


    while (squ > square):
        square += odd
        if (odd == 1):
            series += str(odd)
        else:
            series += " + " + str(odd)
        odd += 2

    series += " = " + str(square)
    print("Input Number =", num)
    
    print(series)
else:
    print("Entered number not in range between 1 and 100")


