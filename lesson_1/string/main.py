# coding: utf-8

# using python 2.7.15
import re

TEXT = (
    "Ten little nigger boys went out to dine; One choked his little self, "
    "and then there were nine. Nine little nigger boys sat up very late; One"
    " overslept himself, and then there were eight. Kight little nigger boys"
    " travelling in Devon; One said he'd stay there,"
    " and then there were seven."
)


# first task
first_string = "qwdbnm,32&32n'43d4f43e4"
first_result = re.findall(r"\d+", first_string)
print first_result, "\n"

# second task
second_string = str(TEXT)
replaces = {
    "One": "1",
    "seven": "7",
    "eight": "8",
    "Eight": "8",
    "nine": "9",
    "Nine": "9",
    "Ten": "10"
}
for old_str, new_str in replaces.items():
    second_string = second_string.replace(old_str, new_str)
print second_string, "\n"

# third task
third_string = str(TEXT)
third_result = re.sub(r"\w{6,}", "", third_string)
print third_result, "\n"

#fourth task
def lower_chars_count(string):
    return len(filter(str.islower, string))

def upper_chars_count(string):
    return len(filter(str.isupper, string))

def chars_count(string):
    return len(filter(str.isalpha, string))


fourth_string = str(TEXT)
lower_chars = lower_chars_count(fourth_string)
upper_chars = upper_chars_count(fourth_string)
all_chars = chars_count(fourth_string) 
print "lower chars: {}%".format(float(lower_chars) / all_chars * 100)
print "upper_chars: {}%".format(float(upper_chars) / all_chars * 100), "\n"

# fifth task
fifth_string = str(TEXT)
sorted_words = fifth_string.split()
sorted_words = sorted(sorted_words, key=len)
print sorted_words, "\n"

# sixth task
sixth_string = str(TEXT)
letters_frequency = []

# seventh task
words_list = ["Ten", "little", "nigger", "boys", "went", "out", "to", "dine"]
seventh_string = " ".join(words_list)
print seventh_string, "\n"

# eighth task
eighth_string = "Hello World!"
print eighth_string[2]
print eighth_string[-2]
print eighth_string[:6]
print eighth_string[:-2]
print eighth_string[::2]
print eighth_string[1::2]
print eighth_string[::-1]
print eighth_string[::-1][::2]
print len(eighth_string)
