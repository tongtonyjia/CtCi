###############################################################################
#
# 1.9 String Rotation
#
# Assume you have a method isSubstring which checks if one world is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a
# rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a
# rotation of "erbottlewat").
#
###############################################################################

s1 = "waterbottle"
s2 = "erbottlewat"


def isSubstring(s1, s2):
    return True


def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return isSubstring(s1+s1, s2)


print isRotation(s1, s2)
