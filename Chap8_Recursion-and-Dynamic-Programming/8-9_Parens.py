###############################################################################
#
# 8.9 Parens
#
# Implement an algorithm to print all valid (i.e., properly opened and closed)
# combinations of n pairs of parenthesis.
#
# EXAMPLE
# Input: 3
# Output: ((())), (()()), (())(), ()(()), ()()()
#
###############################################################################

from copy import deepcopy


def parens_d(n):
    if n == 0:
        return ''
    elif n == 1:
        return '()'

    parenss = dict()
    parenss[1] = set()
    parenss[1].add('()')

    for i in range(2, n+1):
        parenss[i] = set()
        for paren in parenss[i-1]:
            for idx in range(len(paren)):
                new = deepcopy(paren)
                new = new[:idx] + '()' + new[idx:]
                parenss[i].add(new)

    return list(parenss[n])


print parens_d(4)


def _parens(parenss, left_rem, right_rem, paren):
    if left_rem < 0 or right_rem < left_rem:
        return
    if left_rem == 0 and right_rem == 0:
        parenss.append(deepcopy(paren))
    else:
        left = deepcopy(paren) + '('
        _parens(parenss, left_rem-1, right_rem, left)

        right = deepcopy(paren) + ')'
        _parens(parenss, left_rem, right_rem-1, right)


def parens(n):
    paren = ''
    parenss = list()
    _parens(parenss, n, n, paren)
    return parenss

print parens(4)
