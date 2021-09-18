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

# {} is set
# {}.add: value: any(immut) -> void
st = {1, 2}
st.add(3)
print(st)

# {} is set
# {}.copy: void -> {}
# Shallow copy of the set
st2 = st.copy()
print(st2)
print(st2 is st)

# range: (lower: int, upper: int, step: int)) -> int<iterable>
int_iter = range(5)
int_iter_limited = range(5, 8)
int_iter_step = range(1, 10, 2)
print(int_iter)
print(int_iter_limited)
print(int_iter_step)

# enumerate: [] -> (index: int, value: any)
for i, value in enumerate([1, 2, 3]):
    print(i, value)

# iter: <iterable> -> <iterator>
a_dict = {1: 'one', 2: 'two', 3: 'three'}
iterable = a_dict.keys()
iterator = iter(iterable)
print(iterable)
print(iterator)
try:
    iterable[0]
except TypeError as e:
    print('Accessing an iterable via index is not allowed.')

# next: <iterator> -> value: any
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration as e:
    print("After the last value when calling 'next' a StopIteration error is thrown.")

# map: (func, []) -> <map obj<iterable>>
x = map(lambda x: x * 2, [1, 2, 3])
print(x)
x = list(x)
print(x)

# filter: (func, []) -> <filer obj<iterable>>
y = filter(lambda x: x > 5, [3, 4, 5, 6, 7, 8])
print(y)
y = list(y)
print(y)