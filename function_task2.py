import random
import string


# create_random_dict function creates and returns dictionary with random letter keys and random number (0-100) values
def create_random_dict():
    random_dict = {}
    for j in range(random.randint(2, 10)):
        # take random letter from letters string as a key
        key = random.choice(string.ascii_lowercase)
        # take random int value as a value
        value = random.randint(1, 100)
        # write pair in dict
        random_dict[key] = value
    return random_dict

# create_random_list_of_dicts function creates and returns list of random number (2-10) of dictionaries
def create_random_list_of_dicts():
    random_list = []
    for i in range(random.randint(2, 10)):
        # call create_random_dict() function - generate random dictionary
        # add dictionary to the list
        random_list.append(create_random_dict())
    return random_list

# create_common_dict function creates and returns one common dictionary from the list of dictionary and
# if there are the same key in the dictionary it takes max value and rename the key
def create_common_dict(list_of_dict):
    tmp_dict = {}
    common_dict = {}
    # create dictionary of pair key - list of values
    for dictionary in list_of_dict:
        for key, value in dictionary.items():
            tmp_dict.setdefault(key, []).append(value)
    # create common dictionary and rename keys
    for key, value in tmp_dict.items():
        if len(value) > 1:
            common_dict[key + "_" + str(value.index(max(value)) + 1)] = max(value)
        else:
            common_dict[key] = value[0]
    return common_dict

# call create_random_list_of_dict function - generate random list of dictionary
# print the list into the console
print(f'Random list of dictionaries: {create_random_list_of_dicts()}')

# call create_common_dict function with the result of create_random_list_of_dicts as argument
# print the common transformed dictionary
print(f'Common transformed dictionary: {create_common_dict(create_random_list_of_dicts())}')

