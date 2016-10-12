###############################################################################
#
# 1.1 Is Unique
#
# Implement an algorithm to deterine if a string has all unique characters.
# What if you cannot use additional data structures?
#
###############################################################################

uniq_str = "qwertyuiop"
non_uniq_str = "Implement an algorithm to deterine if a string has all "


# O(N)
def check_if_all_unique_init(string):
    chars = dict()
    for char in string:
        if char in chars:
            return False
        else:
            chars[char] = True
    return True


# O(NlogN)
def check_if_all_unique_no_new_data_init(string):
    prev = None
    for char in sorted(string):
        if char == prev:
            return False
        else:
            prev = char
    return True


###############################################################################
# Check for string length first. ASCII has 128 alphabet.
# Use set for check.
###############################################################################


# O(N)
def check_if_all_unique(string):
    if len(string) > 128:
        return False

    chars = set()
    for char in string:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True


# O(NlogN)
def check_if_all_unique_no_new_data(string):
    if len(string) > 128:
        return False

    prev = None
    for char in sorted(string):
        if char == prev:
            return False
        else:
            prev = char
    return True

###############################################################################

print check_if_all_unique(uniq_str)
print check_if_all_unique(non_uniq_str)

print check_if_all_unique_no_new_data(uniq_str)
print check_if_all_unique_no_new_data(non_uniq_str)
