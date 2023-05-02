a = float(input("Please enter a grade between 1 and 4."))
if a == 1:
    print(30)
elif a > 1 and a < 2:
    print(27)
elif a >= 2 and a < 3:
    print(24)
elif a >= 3 and a < 4:
    print(21)
elif a == 4:
    print(18)
elif a > 4:
    print("Fail")
elif a < 1:
    print("Fail")