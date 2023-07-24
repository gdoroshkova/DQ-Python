import re
from operator import index

# create text string with text from the task, use """ for multiline string
text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# take text and convert it to lower case
text = text.lower()

# find all 'iz' misspelling in the text and correct them - replace to 'is'
text = text.replace(' iz ', ' is ')

#  split the text into strings by point character
list_of_strings = text.split('.')
# create empty list for saving transformed strings
list_of_correct_strings = []
# create empty string for adding additional string consists of the last words of each string
last_string = ''
# for loop runs through each string from the list of strings
for string in list_of_strings:
     # take each string from the text, remove all the leading white spaces and capitalize them
     string = string.lstrip().capitalize()
     # add reformed strings to the list_of_correct_strings
     list_of_correct_strings.append(string)
     # split every string into the words by space and save them as a list of the string
     list_of_words = string.split()
     # check if the list of words isn't empty
     if len(list_of_words) > 0:
         # add the last element of the each list of words to last_string
         # len() returns amount of element in the list
         last_string = last_string + list_of_words[len(list_of_words)-1] + ' '
# join all strings to each other and save as a text
text = '. '.join(list_of_correct_strings)
# add additional string to the text
text = text + last_string.capitalize() + '.'
# capitalize the first sentence in the task
# create empty list for saving transformed strings of list
colon_split = []
# split text by colon
for string in text.split(':'):
    # take each string, remove all the leading white spaces and capitalize them
    string = string.lstrip().capitalize()
    # add reformed strings to the list
    colon_split.append(string)
# join transformed strings by colon, end of line and tab characters
text = ':\n\t'.join(colon_split)
print(text)
# create variable for counting white spaces in the result text
counter = 0
# for loop runs through each letter in the text
for letter in text:
    # check if the letter is space
    if letter.isspace():
        # if the letter is space increment counter by 1
        counter = counter+1
print("_____________________________________________")
print("The amount of white spaces in the text is: " + str(counter))



