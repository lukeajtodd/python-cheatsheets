# len: [string, []] -> int
print(len('Hello World'))
print(len([1, 2]))

# print: (any, end) -> string
print('HI')
print(15)
print("Hi There", end="!") # end is usually a newline \n

# input: string -> void
# Takes input from the user and accepts a message to show
print(input('Some input: '))

# [].append: any -> void
li = []
li.append(1)
print(li)

# [].pop: void -> any
lis = [1]
print(lis.pop())

# [].remove: value: int -> void
# Remove first instance of a value
lt = [1, 2, 3]
lt.remove(2)
print(lt)

# [].insert: (index: int, value: int) -> void
lt.insert(1, 2)
print(lt)

# [].index: value: int -> index: int
print(lt.index(2))