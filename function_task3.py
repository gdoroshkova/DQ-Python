import re
from operator import index

# create text string with text from the task, use """ for multiline string
text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 
	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 
	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# text_to_lower_case function transforms text to lower case and returns it
def text_to_lower_case(text):
    text = text.lower()
    return text

# correct_misspelling function finds all 'iz' misspelling in the text, corrects them and returns the correct text
def correct_misspelling(text):
    text = text.replace(' iz ', ' is ')
    return text

# create_add_string function creates additional string with last words of each sentence, capitalizes sentences
# and adds additional string to the text
def create_add_string(text):
    list_of_strings = text.split('.')
    list_of_correct_strings = []
    last_string = ''
    for string in list_of_strings:
        string = string.lstrip().capitalize()
        list_of_correct_strings.append(string)
        list_of_words = string.split()
        if len(list_of_words) > 0:
            last_string = last_string + list_of_words[len(list_of_words)-1] + ' '
    text = '. '.join(list_of_correct_strings)
    text = text + last_string.capitalize() + '.'
    return text

# whitespaces_counter function counts and returns number of white spaces in the text
def whitespaces_counter(text):
    counter = 0
    for letter in text:
        if letter.isspace():
            counter = counter+1
    return counter

# call functions in turn and transformed the text
# save transformed text into transformed_text variable
transformed_text = create_add_string(correct_misspelling(text_to_lower_case(text)))
# print transformed text into console
print(f'Transformed text: {transformed_text}')

print("_____________________________________________________")

# call whitespaces_counter function with the transformed_text argument
# print it into the console
print(f'The number of the whitespaces in the correct text: {whitespaces_counter(transformed_text)}')



