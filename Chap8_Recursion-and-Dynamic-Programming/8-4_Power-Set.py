###############################################################################
#
# 8.4 Power Set
#
# Write a method to return all subsets of a set.
#
###############################################################################


def power_set_r(s):
    combs = list()

    for i in range(len(s)):
        new_combs = list()
        for comb in combs:
            new_combs.append(comb + [s[i]])
        combs.append([s[i]])
        combs += new_combs

    combs.append([])
    return combs


s = [-3, 0, 2, 5, 9, 18, 49]
sss = power_set_r(s)
print len(sss)
for ss in sss:
    print ss
