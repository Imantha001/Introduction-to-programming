amount = 0

amount=int(input("Enter the amount? "))

if( amount > 1000 ):
    print("Enter an amount less than 1000")
else:
    n500 = amount // 500
    print(n500," Note(s) of 500.00")
    n100 = (amount% 500) // 100
    print(n100," Note(s) of 100.00")
    n50 = ( amount % 500 % 100) // 50
    print(n50," Note(s) of 50.00")
    n20 = ( amount %500 % 100 %50) // 20
    print(n20," Note(s) of 20.00")
    n10 = ( amount % 500 % 100 % 50 % 20 ) // 10
    print(n10," Note(s) of 10.00")
    n5 = ( amount % 500 % 100 % 50 % 20 % 10) // 5
    print(n5," Note(s) of 5.00")
    n1 = (amount % 500 % 100 % 50 %20 % 10% 5) //1
    print(n1," Note(s) of 1.00")

