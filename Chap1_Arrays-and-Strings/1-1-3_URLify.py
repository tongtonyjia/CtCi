###############################################################################
#
# 1.3 URLify
#
# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficientb space at the end to hold the additional
# characters, and that you are given the "true" lenth of the string.
#
###############################################################################


string = "Mr John Smith    "
true_length = 13


def urlify(str):
    return str.strip().replace(' ', '%20')


print string
print urlify(string)
