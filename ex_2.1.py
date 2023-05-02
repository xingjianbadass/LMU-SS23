a = int(input("Please enter your age: "))
b = 18
if a < b:
    print("You will turn 18 in " + str(b - a) + " years.")
elif a == b:
        print("You are 18!")
elif a > b:
    print("You turned 18 " + str(a - b) + " years ago.")
