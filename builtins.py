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

# {}.keys: void -> list-like
# Returns a list of the dicts keys
# Python 3.7< - Could be random order
# Python 3.7> - Guaranteed order
dict = {1: 1, 2: 2, 3: 3 }
print(dict.keys())

# This needs to be converted to a list with "list"
print(list(dict.keys()))

# {}.keys: void -> list-like
# Returns a list of the dicts values
# Python 3.7< - Could be random order
# Python 3.7> - Guaranteed order
print(dict.values())

# This needs to be converted to a list with "list"
print(list(dict.values()))

# {}.,get: (key: any, default?: any) -> value: any | None
print(dict.get(1))
print(dict.get(4))
print(dict.get(4, 'not there boss'))

# {}.setdefault: (key: any, value: any) -> void
print(dict.setdefault(4, 4))
print(dict.setdefault(4, 5)) # Will stay as 4

# {}.update: dict: {} -> updated_dict: {}
dict.update({ 5: 5 })
print(dict)