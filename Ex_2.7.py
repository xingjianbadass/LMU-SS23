from random import randint
start = 0
end = 30
number_1 = randint(start, end)
number_2 = randint(start, end)
print(number_1)
print(number_2)
if number_1 > number_2:
    number_1 = 2 * number_1
    start = 2 * start
    end = 2 * end
    number_2 = number_2 + randint(start, end)
    if number_1 < number_2:
        score_difference = number_2 - number_1
        print("I finally beat you, my score was greater than yours by " + str(score_difference) + " points.")
    elif number_1 > number_2:
        number_1 = number_1 // 2
        if number_1 > number_2:
            print("I cannot beat you.")
        elif number_1 < number_2:
            score_difference = number_2 - number_1
            print("I finally beat you, my score was greater than yours by " + str(score_difference) + " points.")
elif number_2 > number_1:
    number_2 = 2 * number_2
    start = 2 * start
    end = 2 * end
    number_1 = number_1 + randint(start, end)
    if number_2 < number_1:
        score_difference = number_1 - number_2
        print("I finally beat you, my score was greater than yours by " + str(score_difference) + " points.")
    elif number_2 > number_1:
        number_2 = number_2 // 2
        if number_2 > number_1:
            print("I cannot beat you.")
        elif number_2 < number_1:
            score_difference = number_1 - number_2
            print("I finally beat you, my score was greater than yours by " + str(score_difference) + " points.")
            