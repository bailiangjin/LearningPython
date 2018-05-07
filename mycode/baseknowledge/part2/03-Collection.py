L = [123, 'spam', 1.23]  # A list of three different-type objects

print(L)
print(len(L))  # Number of items in the list

print(L[0])  # Indexing by position

print(L[:-1])  # 切分list # Slicing a list returns a new list

print(L + [4, 5, 6])  # 创建了一个新的list # Concatenation makes a new list too

print(L)  # 原list并未改变  We're not changing the original list

L.append('NI')  # 添加元素 原list才会改变 # Growing: add object at end of list
print(L)

print("删除元素:" + str(L.pop(2)))  # 删除指定位置的元素 # Shrinking: delete an item in the middle

print(L)  # "del L[2]" deletes from a list too

M = ['bb', 'aa', 'cc']
print(M)

M.sort()  # 排序
print(M)

M.reverse()  # 反转
print(M)

print(L)

# 角标越界

# print(L[99])

# L[99] = 1

#### 嵌套数组 矩阵


M = [[1, 2, 3],  # A 3 � 3 matrix, as nested lists
     [4, 5, 6],  # Code can span lines if bracketed
     [7, 8, 9]]
print(M)
print(M[1])  # Get row 2

print(M[1][2])  # Get row 2, then get item 3 within the row

# 列表解析

col2 = [row[1] for row in M]  # Collect the items in column 2
print(col2)
print(M)  # The matrix is unchanged

print([row[1] + 1 for row in M])  # Add 1 to each item in column 2

print([row[1] for row in M if row[1] % 2 == 0])  # Filter out odd items

diag = [M[i][i] for i in [0, 1, 2]]  # Collect a diagonal from matrix
print(diag)

doubles = [c * 2 for c in 'spam']  # Repeat characters in a string
print(doubles)

# Note: see later in the book for more on the iteration protocol; its
# full realization is: G = (...); I = iter(G); I.next() until StopIteration;
# generators are their own iterator (iter(G) returns G itself), so the iter(G)
# call described later in this chapter is not required in the following; 

G = (sum(row) for row in M)  # Create a generator of row sums

print(G)
print(next(G))
print(next(G))  # Run the iteration protocol

print(list(map(sum, M)))  # Map sum over items in M

print({sum(row) for row in M})  # Create a set of row sums

print({i: sum(M[i]) for i in range(3)})  # Creates key/value table of row sums

print([ord(x) for x in 'spaam'])  # List of character ordinals
print({ord(x) for x in 'spaam'})  # Sets remove duplicates 不同之处 这个是大括号 上一个是中括号

print({x: ord(x) for x in 'spaam'})  # Dictionary keys are unique
