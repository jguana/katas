#
# Complete the solution so that it splits the string into pairs of two
# characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').
#
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def solution(s):
    if len(s) % 2 != 0:
        s = s + '_'
    pairs = []
    while s:
        pairs.append(s[:2])
        s = s[2:]
    return pairs

print(solution('abc'))
