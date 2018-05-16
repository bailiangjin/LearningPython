D = {'spam': 2, 'ham': 1, 'eggs': 3}  # Make a dictionary
print(D['spam'])  # Fetch a value by key
# 2
print(D)  # Order is scrambled
# {'eggs': 3, 'ham': 1, 'spam': 2}
# 
print(len(D))  # Number of entries in dictionary
# 3
print('ham' in D)  # Key membership test alternative
# True
print(list(D.keys()))  # Create a new list of my keys
# ['eggs', 'ham', 'spam']
# 
# D
# {'eggs': 3, 'ham': 1, 'spam': 2}
# 
D['ham'] = ['grill', 'bake', 'fry']  # Change entry
print(D)
# {'eggs': 3, 'ham': ['grill', 'bake', 'fry'], 'spam': 2}
# 
del D['eggs']  # Delete entry
print(D)
# {'ham': ['grill', 'bake', 'fry'], 'spam': 2}
# 
D['brunch'] = 'Bacon'  # Add new entry
print(D)
# {'brunch': 'Bacon', 'ham': ['grill', 'bake', 'fry'], 'spam': 2}
# 
D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.values()))
# [3, 1, 2]
print(list(D.items()))
# [('eggs', 3), ('ham', 1), ('spam', 2)]
# 
print(D.get('spam'))  # A key that is there
print(D.get('not_exist'))  # A key that is there
# 2
print(D.get('toast'))  # A key that is missing
# None
print(D.get('toast', 88))

# 88
print(D.get('toast'))
# 
print(D)
# {'eggs': 3, 'ham': 1, 'spam': 2}
D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)
# {'toast': 4, 'muffin': 5, 'eggs': 3, 'ham': 1, 'spam': 2}
# 
# # pop a dictionary by key
print(D)
# {'toast': 4, 'muffin': 5, 'eggs': 3, 'ham': 1, 'spam': 2}
print(D.pop('muffin'))
# 5
print(D.pop('toast'))  # Delete and return from a key
# 4
print(D)
# {'eggs': 3, 'ham': 1, 'spam': 2}
# 
# # pop a list by position
L = ['aa', 'bb', 'cc', 'dd']
print(L)
print(L.pop())  # Delete and return from the end
# 'dd'
print(L)
# ['aa', 'bb', 'cc']
print(L.pop(1))  # Delete from a specific position
# 'bb'
print(L)
# ['aa', 'cc']
# 
table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout'}
# 
language = 'Python'
creator = table[language]
print(creator)
# 'Guido van Rossum'
# 
for lang in table:  # Same as: for lang in table.keys()
    ...
    print(lang, '\t', table[lang])

# 
L = []
# L[99] = 'spam'
print(L)

# 
D = {}
D[99] = 'spam'
print(D[99])
# 'spam'
print(D)
# {99: 'spam'}


Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2;
Y = 3;
Z = 4  # ; separates statements
print(Matrix[(X, Y, Z)])
print(Matrix)
# {(2, 3, 4): 88, (7, 8, 9): 99}
#
# print(Matrix[(2, 3, 6)])
# Traceback (most recent call last):
# 2
#   File "/Users/bailiangjin/dev/workspace/kevinswork/python/study/LearningPython/mycode/baseknowledge/part2/04-Dictionary.py", line 111, in <module>
# {'spam': 2, 'ham': 1, 'eggs': 3}
# 3
#     print(Matrix[(2, 3, 6)])
# True
# KeyError: (2, 3, 6)


#
if (2, 3, 6) in Matrix:  # Check for key before fetch
    ...
    print(Matrix[(2, 3, 6)])  # See Chapter 12 for if/else
else:
    print(0)
# ...
# 0
try:
    ...
    print(Matrix[(2, 3, 6)])  # Try to index
except KeyError:  # Catch and recover

    print(0)  # See Chapter 33 for try/except
# ...
# 0
print(Matrix.get((2, 3, 4), 0))  # Exists; fetch and return
# 88
print(Matrix.get((2, 3, 6), 0))  # Doesn't exist; use default arg
# 0
#
rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'
# >> >
print(rec['name'])
# mel
#
mel = {'name': 'Mark',
       'jobs': ['trainer', 'writer'],
       'web': 'www.rmi.net/�lutz',
       'home': {'state': 'CO', 'zip': 80513}}

print(mel)
#
print(mel['name'])
# 'Mark'
print(mel['jobs'])
# ['trainer', 'writer']
print(mel['jobs'][1])
# 'writer'
print(mel['home']['zip'])
# 80513
#
# # NOTE: in the following, you must use "dbm" instead of "anydbm"
# # in Python 3.X (this module was renamed in 3.X only).  Also note
# # that these are incomplete, partial examples as is.
#

# 使用数据库
# import dbm
#
# file = dbm.open("filename")  # Link to file
# file['key'] = 'data'  # Store data by key
# data = file['key']  # Fetch data by key
# print(data)
#
# import cgi
#
# form = cgi.FieldStorage()  # Parse form data
# if 'name' in form:
#     showReply('Hello, ' + form['name'].value)
#
print({'name': 'mel', 'age': 45})  # Traditional literal expression

D = {}  # Assign by keys dynamically
D['name'] = 'mel'
D['age'] = 45

print(D)
# dict(name='mel', age=45)  # dict keyword argument form

print(dict([('name', 'mel'), ('age', 45)]))  # dict key/value tuples form

print(dict.fromkeys(['a', 'b'], 0))
# {'a': 0, 'b': 0}
#
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))  # Zip together keys and values
# [('a', 1), ('b', 2), ('c', 3)]
#
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  # Make a dict from zip result
print(D)
# {'a': 1, 'c': 3, 'b': 2}
#
# C:\misc > c:\python30\python  # dict comprehension
#
D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)
# {'a': 1, 'c': 3, 'b': 2}
#
D = {x: x ** 2 for x in [1, 2, 3, 4]}  # Or: range(1, 5)
print(D)
# {1: 1, 2: 4, 3: 9, 4: 16}
#
D = {c: c * 4 for c in 'SPAM'}  # Loop over any iterable
print(D)
# {'A': 'AAAA', 'P': 'PPPP', 'S': 'SSSS', 'M': 'MMMM'}
#
D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
# {'eggs': 'EGGS!', 'ham': 'HAM!', 'spam': 'SPAM!'}
#
D = dict.fromkeys(['a', 'b', 'c'], 0)  # Initialize dict from keys
print(D)
# {'a': 0, 'c': 0, 'b': 0}
#
D = {k: 0 for k in ['a', 'b', 'c']}  # Same, but with a comprehension
print(D)
# {'a': 0, 'c': 0, 'b': 0}
#
D = dict.fromkeys('spam')  # Other iterators, default value
print(D)
# {'a': None, 'p': None, 's': None, 'm': None}
#
D = {k: None for k in 'spam'}
print(D)
# {'a': None, 'p': None, 's': None, 'm': None}
#
# D = dict(a=1, b=2, c=3)
# #D
# {'a': 1, 'c': 3, 'b': 2}
#
# #K = D.keys()  # Makes a view object in 3.0, not a list
# #K
# < dict_keys
# object
# at
# 0x026D83C0 >
# #list(K)  # Force a real list in 3.0 if needed
# ['a', 'c', 'b']
#
# #V = D.values()  # Ditto for values and items views
# #V
# < dict_values
# object
# at
# 0x026D8260 >
# #list(V)
# [1, 3, 2]
#
# #list(D.items())
# [('a', 1), ('c', 3), ('b', 2)]
#
# #K[0]  # List operations fail unless converted
# TypeError: 'dict_keys'
# object
# does
# not support
# indexing
# #list(K)[0]
# 'a'
#
# #for k in D.keys(): print(k)  # Iterators used automatically in loops
# ...
# a
# c
# b
#
# #for key in D: print(key)  # Still no need to call keys() to iterate
# ...
# a
# c
# b
#
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
# {'a': 1, 'c': 3, 'b': 2}
#
K = D.keys()
V = D.values()
print(list(K))  # Views maintain same order as dictionary
# ['a', 'c', 'b']
print(list(V))
# [1, 3, 2]
#
del D['b']  # Change the dictionary in-place
print(D)
# {'a': 1, 'c': 3}
#
print(list(K))  # Reflected in any current view objects
# ['a', 'c']
print(list(V))  # Not true in 2.X!
# [1, 3]
#
K | {'x': 4}  # Keys (and some items) views are set-like
print(K)
# {'a', 'x', 'c'}
#
# V & {'x': 4}
# TypeError: unsupported
# operand
# type(s)
# for &: 'dict_values' and 'dict'
# #V & {'x': 4}.values()
# TypeError: unsupported
# operand
# type(s)
# for &: 'dict_values' and 'dict_values'
#
D = {'a': 1, 'b': 2, 'c': 3}
D.keys() & D.keys()  # Intersect keys views
# {'a', 'c', 'b'}
D.keys() & {'b'}  # Intersect keys and set
print(D.keys())
# {'b'}
D.keys() & {'b': 1}  # Intersect keys and dict
print(D)
# {'b'}
print(D.keys() | {'b', 'c', 'd'})  # Union keys and set
# {'a', 'c', 'b', 'd'}
#
D = {'a': 1}
print(list(D.items()))  # Items set-like if hashable
# [('a', 1)]
print(D.items() | D.keys())  # Union view and view
# {('a', 1), 'a'}
print(D.items() | D)  # dict treated same as its keys
# {('a', 1), 'a'}
print(D.items() | {('c', 3), ('d', 4)})  # Set of key/value pairs
# {('a', 1), ('d', 4), ('c', 3)}
print(dict(D.items() | {('c', 3), ('d', 4)}))  # dict accepts iterable sets too
# {'a': 1, 'c': 3, 'd': 4}
#
D = {'a': 1, 'b': 2, 'c': 3}
print(D)
# {'a': 1, 'c': 3, 'b': 2}
#
Ks = D.keys()  # Sorting a view object doesn't work!
print(Ks)
# Ks.sort() # 3.0版本不可用
# print('sorted:' + Ks)
# AttributeError: 'dict_keys'
# object
# has
# no
# attribute
# 'sort'
#
Ks = list(Ks)  # Force it to be a list and then sort
Ks.sort()
for k in Ks: print(k, D[k])
# ...
# a
# 1
# b
# 2
# c
# 3
#
print(D)
# {'a': 1, 'c': 3, 'b': 2}
Ks = D.keys()  # Or you can use sorted() on the keys
for k in sorted(Ks): print(k, D[k])  # sorted() accepts any iterable
# ...  # sorted() returns its result
# a
# 1
# b
# 2
# c
# 3
#
# #D
# {'a': 1, 'c': 3, 'b': 2}  # Better yet, sort the dict directly
for k in sorted(D): print(k, D[k])  # dict iterators return keys
# ...
# a
# 1
# b
# 2
# c
# 3
#
print(sorted(D.items()) < sorted(D2.items()) ) # Like 2.6 D1 < D2
#
print(D)
# {'a': 1, 'c': 3, 'b': 2}
# print(D.has_key('c'))  # 2.X only: True/False
# AttributeError: 'dict'
# object
# has
# no
# attribute
# 'has_key'
print('c' in D)
# True
print('x' in D)
# False
if 'c' in D: print('present', D['c'])  # Preferred in 3.0
# ...
# present
# 3
#
print(D.get('c'))
# 3
print(D.get('x'))
# None
if D.get('c') != None: print('present', D['c'])  # Another option
# ...
#
