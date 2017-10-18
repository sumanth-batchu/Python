count = 0


def persistence(num):  # this is a function which returns multiplicative persistence of a number
    product = 1
    for i in num:  # finding the product of digits in a number
        product = product * int(i)

    global count

    if len(num) == 1:  # if the given input is a single digit it straight away returns the count
        return count
    elif product < 10:  # it increments the count by each step
        count += 1
        return count
    else:
        count += 1
        return persistence(str(product))  # recursive call to find the multiplicative persistence

print(persistence(str(input("Enter a number:"))))  # this statement combines to take input from the user and passes it
                                                   # as the function argument
