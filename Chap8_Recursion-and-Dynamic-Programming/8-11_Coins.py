###############################################################################
#
# 8.11 Coins:
#
# Given an infinite number of quarter (25 cents), dimes (10 cents), nickels (5
# cents), and pennies (1 cent), write code to calculate the number of ways of
# representing n cents.
#
###############################################################################

from copy import deepcopy


def _count_coins_ways(n, coin_types, ways, coins):
    for coin in coin_types:
        _coins = deepcopy(coins)
        _coins.append(coin)

        if sum(_coins) == n:
            coin_way = list()
            for coin_type in coin_types:
                coin_way.append(_coins.count(coin_type))
            ways.add(str(coin_way))
        elif sum(_coins) > n:
            continue
        else:
            _count_coins_ways(n, coin_types, ways, _coins)


def count_coins_ways(n):
    if n == 0:
        return 0

    coin_types = [25, 10, 5, 1]

    ways = set()

    _count_coins_ways(n, coin_types, ways, [])

    return ways


ways = count_coins_ways(27)
print 'Ways: {}\n'.format(len(ways))
for way in sorted(list(ways)):
    print way
