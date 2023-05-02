a = int(input("Please enter one number."))
b = int(input("Please enter another number."))
if a % 2 == 0 and b % 2 == 0:
    print(a + b)
elif a % 2 == 1 and b % 2 == 1:
    print(a - b)
elif a % 2 == 1 and b % 2 == 0:
    print(a * b)
elif a % 2 == 0 and b % 2 == 1:
    print(a * b)
