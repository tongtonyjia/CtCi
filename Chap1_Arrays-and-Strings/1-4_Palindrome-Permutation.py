###############################################################################
#
# 1.4 Palindrome Permutation
#
# Given a string, write a function to check if it is a permuation of a
# palindrome. A palinedrome is a work or phrase that is the same forwards and
# backwards. A permuatation is a rearrangelment of letters. The palindrome
# does not need to be limited to just dictionary words.
#
###############################################################################


string = "Tact Coa"


# O(N)
def palin_permu(str):
    char_nums = dict()
    for char in string.lower():
        if char == ' ':
            continue
        if char in char_nums:
            char_nums[char] += 1
        else:
            char_nums[char] = 1

    count_odd = 0
    for num in char_nums.itervalues():
        if num % 2 != 0:
            count_odd += 1
            if count_odd > 1:
                return False

    return True


print string
print palin_permu(string)


# Alternative solution would be to use bits for keeping track of char counts.
