# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']

def unique_in_order(iterable):
    res = []
    for c in iterable:
        if len(res) == 0 or res[-1] != c:
            res.append(c)
    return res

print(unique_in_order('AAAABBBCCDAABBB'))
