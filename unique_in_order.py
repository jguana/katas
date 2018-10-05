# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
def unique_in_order(iterable):
    result = [iterable[0]]
    prev = iterable[0]
    for item in iterable:
        if item != prev:
            result.append(item)
            print(result)
        prev = item

    return result




print(unique_in_order('AAAABBBCCDAABBB'))
