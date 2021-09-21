from collections import Counter


def sockMerchant(n, ar):
    even = 0
    ar.sort()
    uniq = Counter(ar)
    for u in uniq:
        even += uniq[u] / 2
    return even

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])