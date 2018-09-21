# vowels list
pyList = ['e', 'a', 'u', 'o', 'i']
print(sorted(pyList))

# string
pyString = 'Python'
print(sorted(pyString))

# vowels tuple
pyTuple = ('e', 'a', 'u', 'o', 'i')
print(sorted(pyTuple))

# take second elemnt for sort
def takeSecond(elem):
    return elem[1]

# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

sortedList2 = sorted(random)
# sort list with key
sortedList = sorted(random, key=takeSecond)


# print list
print('Sorted list:', sortedList2)
print('Sorted list:', sortedList)

w = "as1d"
print(sorted(w))
