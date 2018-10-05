# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
def not_duplicate(x,y):
    # returns true if not duplicate
    if x != y:
        return True
    return False

def unique_in_order(iterable):
    filtered = filter(lambda x, y: not_duplicate(x, y), iterable)
    print(reduced)


unique_in_order('AAAABBBCCDAABBB')
