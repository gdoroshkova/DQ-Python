import random
# create list of 100 random numbers from 0 to 1000
# range(1001) creates a sequence of numbers from 0 to 1000.
# The random.sample() function then selects 100 unique elements from this range
random_numbers = random.sample(range(1001), 100)
print(random_numbers)
# sort list from min to max (without using sort())
# assign 0 to min_index - index of the 1st element from the list
min_index = 0
# The first For loop takes elements from the list beginning from the 1st one
# The second For loop takes elements from the list beginning from the 2nd one
for i in range(0, len(random_numbers)):
    # in the first loop run assign 1st element from the list to min_element
    min_element = random_numbers[i]
    for j in range(i+1, len(random_numbers)):
        # compare current and the next elements with each other
        if random_numbers[j] < random_numbers[i]:
            # if the condition is true reassign min_index and min_element
            min_index = j
            min_element = random_numbers[j]
            # swap current and the next elements
            random_numbers[j] = random_numbers[i]
            random_numbers[i] = min_element
print(random_numbers)
# calculate average for even and odd numbers
# create variables for saving sum and amount of even and odd numbers
sum_of_even = 0
amount_of_even = 0
sum_of_odd = 0
amount_of_odd = 0
# For loop takes elements from the list beginning from the 1st one
for i in range(0, len(random_numbers)):
    # check if number is even
    if random_numbers[i] % 2 == 0:
        # if condition is true change the sum_of_even and amount_of_even
        sum_of_even = sum_of_even + random_numbers[i]
        amount_of_even = amount_of_even + 1
    else:
        # if condition is false and number is odd change the sum_of_odd and amount_of_odd
        sum_of_odd = sum_of_odd + random_numbers[i]
        amount_of_odd = amount_of_odd + 1
# print both average result in console
# The format() insert values inside the string's placeholder that defined using {}
# The round() rounds average values to 2 digits
print("The average for even numbers is: {}. The average for odd number is: {}".format(round(sum_of_even / amount_of_even, 2), round(sum_of_odd / amount_of_odd, 2)))



