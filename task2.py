import random
import string

# create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),

# string of all lowercase letters of the alphabet
letters = string.ascii_lowercase
# create empty list
list_of_dict = []
# First For loop creates random numbers of dict
for i in range(random.randint(2, 10)):
    random_dic = {}
    # For loop fils dict with random letter key and random int value
    for j in range(random.randint(2, 10)):
        # take random letter from letters string as a key
        key = random.choice(letters)
        # take random int value as a value
        value = random.randint(1, 100)
        # write pair in dict
        random_dic[key] = value
    # add dict to the list
    list_of_dict.append(random_dic)
print(list_of_dict)

# get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# create empty common_dict to write result dict from
common_dict = {}
# create empty temp_dict to rewrite list of dicts to dict of lists
temp_dict = {}
# transform list of dicts into dict of lists
# run through each dictionary from the list
for dictionary in list_of_dict:
    # run through each key-value pair from dictionary
    for key, value in dictionary.items():
        # setdefault() insert the key and empty list of value
        # append() adds value to the end of the list
        temp_dict.setdefault(key, []).append(value)

# selection the biggest value from each list of value for each key
# run through each key-value pair from temp_dict
for key, value in temp_dict.items():
    # check if the list contains more than 1 value
    if len(value) > 1:
        # record element with the max value from the list of values to the common_dict and rewrite key
        # index() returns the position of value
        # max() returns the highest value
        common_dict[key+"_"+str(value.index(max(value))+1)] = max(value)
    # if the list of value consists of 1 value
    else:
        # record the key-value pair to the common_dict
        common_dict[key] = value[0]
print(common_dict)



