###############################################################################
#
# 1.6 String Compression
#
# Implement a method to perform basic string compression using the counts of
# repeated characters, For example, the string aabcccccaaa would become
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string. You can
# assume the string has only uppercase and lowercase letters (a-z).
#
###############################################################################


string1 = "aabcccccaaa"
string2 = "aabcaa"


# O(N)
def compress_string(string):
    str_len = len(string)

    comp_str = ''

    worth = False
    count = 1
    append_action = False
    for i in range(1, str_len):
        if string[i] == string[i-1]:
            count += 1
            if i != str_len-1:
                continue
            else:
                append_action = True
        else:
            append_action = True

        if append_action:
            if count > 1:
                comp_str = comp_str + string[i-1] + str(count)
                if count > 2:
                    worth = True
            else:
                comp_str += string[i-1]
            count = 1
            append_action = False

    if worth:
        return comp_str
    else:
        return string


print string1
print compress_string(string1)
print ''
print string2
print compress_string(string2)
