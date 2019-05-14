# Define a function that accepts a list of numbers as an argument and returns the sum of the odd numbers in the list.
#Test it to make sure it works.

def any_number(numbers):
    sum = 0
    for number in numbers:
        if number % 2 != 0:
            sum += number
        else:
            continue
    return sum
print(any_number([15, 8, 10]))