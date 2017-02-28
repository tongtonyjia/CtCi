###############################################################################
#
# 8.8 Permutations with Dups
#
# Write a method to compute all permutations of a string whose characters are
# not necessarily unique. The list of permutations should not have duplicates.
#
###############################################################################

from copy import deepcopy


s = 'asda'


def permu_d(s):
    perms = list()
    perms_map = set()
    char_map = dict()

    for c in s:
        if c not in char_map:
            char_map[c] = 1
        else:
            char_map[c] += 1
        if c in perms_map:
            continue
        perms_map.add(c)
        perms.append(c)

    idx = 0
    while len(perms[idx]) != len(s):
        perm = perms[idx]

        for c in s:
            if perm.count(c) != char_map[c]:
                new = deepcopy(perm)
                new += c
                if new in perms_map:
                    continue
                perms.append(new)
                perms_map.add(new)

        idx += 1

    return perms[idx:]


for row in permu_d(s):
    print row
