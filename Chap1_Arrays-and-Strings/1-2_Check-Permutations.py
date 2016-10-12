###############################################################################
#
# 1.2 Check Permutations
#
# Given two strings, wrtie a method to decide if one is a permutation of the
# other.
#
###############################################################################

string1 = "lalaland"
string2 = "lalandla"
string3 = "lalandll"


# O(NlogN)
def if_permu(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


# O(N)
def if_permu_with_dict(str1, str2):
    if len(str1) != len(str2):
        return False

    chars = dict()
    for char in str1:
        if char in chars:
            chars[char] = chars[char] + 1
        else:
            chars[char] = 1

    for char in str2:
        if char in chars:
            chars[char] = chars[char] - 1
            if chars[char] < 0:
                return False
        else:
            return False

    return True


print if_permu(string1, string2)
print if_permu(string1, string3)

print if_permu_with_dict(string1, string2)
print if_permu_with_dict(string1, string3)
