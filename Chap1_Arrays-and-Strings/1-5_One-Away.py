###############################################################################
#
# 1.5 One Away
#
# There ar three types of edit that can be performed on strings: insert a
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.
#
###############################################################################


string1 = "pale"
string2 = "ple"
string3 = "pales"
string4 = "bale"
string5 = "bake"
string6 = "ealp"


# IF CAN CHANGE ORDERING FOR FREE (WRONG!!!)
def if_one_edit_reorder(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    str1_dict = dict()
    for char in str1:
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1
    diffs = 0
    for char in str2:
        if char in str1_dict:
            str1_dict[char] -= 1
            if str1_dict < 0:
                diffs += 1
        else:
            diffs += 1

    return (diffs < 2)


# O(N)
def if_one_edit(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)
    if abs(str1_len - str2_len) > 1:
        return False

    diff_count = 0
    if str1_len == str2_len:
        for i in range(str1_len):
            if str1[i] != str2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
                else:
                    i += 1
    else:
        if str1_len < str2_len:
            short_str = str1
            short_str_len = str1_len
            long_str = str2

        else:
            short_str = str2
            short_str_len = str2_len
            long_str = str1

        j = 0
        for i in range(short_str_len):
            if short_str[i] != long_str[j]:
                diff_count += 1
                if diff_count > 1:
                    return False
                j += 1
            j += 1

    return True

print if_one_edit(string1, string2)
print if_one_edit(string1, string3)
print if_one_edit(string1, string4)
print if_one_edit(string1, string5)
print if_one_edit(string1, string6)
