print((1, 2) + (3, 4))  # Concatenation
# (1, 2, 3, 4)
# 
print((1, 2) * 4)  # Repetition
# (1, 2, 1, 2, 1, 2, 1, 2)
# 
T = (1, 2, 3, 4)  # Indexing, slicing
print(T[0], T[1:3])
# (1, (2, 3))
# 
# 
# 
x = (40)  # An integer!
print(x)
# 40
y = (40,)  # A tuple containing an integer
print(y)
# (40,)
# 
# 
# 
T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)  # Make a list from a tuple's items
print(tmp)
tmp.sort()  # Sort the list

print(tmp)
# ['aa', 'bb', 'cc', 'dd']
T = tuple(tmp)  # Make a tuple from the list's items
print(T)
# ('aa', 'bb', 'cc', 'dd')
# 
print(sorted(T))  # Or use the sorted built-in
# ['aa', 'bb', 'cc', 'dd']
# 
# 
# 
T = (1, 2, 3, 4, 5)
print(T)
L = [x + 20 for x in T]
print(L)
# [21, 22, 23, 24, 25]
# 
# 
# 
T = (1, 2, 3, 2, 4, 2)       # Tuple methods in 2.6 and 3.0
print(T.index(2))                   # Offset of first appearance of 2
# 1
print(T.index(2, 2))                # Offset of appearance after offset 2
# 3
print(T.count(2))                   # How many 2s are there?
# 3
# 
# 
# 
T = (1, [2, 3], 4)
print(T)
# T[1] = 'spam'                # This fails: can't change tuple itself
# TypeError: object doesn't support item assignment

T[1][0] = 'spam'             # This works: can change mutables inside
print(T)
# (1, ['spam', 3], 4)
