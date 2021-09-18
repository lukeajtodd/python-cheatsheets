# Division results in a float
print("Division results in a float: \n")
print(10 / 3)
print("\n")

# You can negate a boolean with "not"
print("Uou can negate a boolean with 'not': \n")
print(not False)
print("\n")

# Boolean operators are words
print("Boolean operators are words: \n")
print(True and False)
print(False or True)
print("\n")

# True and False are actually 1 and 0
print("True and False are equivalent to 1 and 0: \n")
print(True + True)
print("\n")

# Comparison looks at the numerical value of True and False
print("Comparison looks at the numerical value of True and False: \n")
print(0 == False)
print(1 == True)
print(2 == True)
print("\n")

# Casting an "int" to bool swaps them to a bool but returns their original value when compared
print("Casting to bool swaps but retains original value: \n")
print(bool(0))
print("\n")

# > >= < <= can be chained
print("GT and LT can be chained: \n")
print(1 < 2 < 3)
print("\n")

# == for equality and "is" for actually sameness
print("== is for equality and 'is' is for sameness\n")
a = [1, 2]
b = a
print(a is b) # True
print(a == b) # True
b = [1, 2]
print(b is a) # False
print(b == a) # True
print("\n")

# Strings can be accessed via int indexes
print("Strings can be accessed via index: \n")
print("Hello"[0])
print("\n")

# f-strings are super good for string interpolation
print("f-strings are neat: \n")
name = 'Jimmy'
print(f"Hello {name}")
print(f'Hello {name}')
print("\n")

# None is the nullish equivalent (it is still an object)
print("None is the nullish equivalent: \n")
print(None)
print(None is None)
print(None == None)
print("\n")

# What evaluates to False
print("These evaluate to False, everything else is True: \n")
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))
print("\n")

# if can be an expression
print("'if' can be an expression: \n")
print("yay!" if 0 > 1 else "nay!")
print("\n")

# Can access values in a list using negative indexes
print("Negative indexes to access a list backwards: \n")
li = [1, 2, 3]
print(li[-1])
print(li[-2])
print("\n")

# Take a slice of a list with [X:Y:Z]
# X is start (included)
# Y is end (excluded)
# Z is step
print("Slices can be taken from a list using [X:Y:Z]: \n")
lis = [1, 2, 3, 4, 5]
print(lis[1:2])
print(lis[:2])
print(lis[::2])
print(lis[::-1]) # Reverse the list
print("\n")

# Copying a list only shallowly copies (they aren't the same as a result)
print("Lists can be copied with [:]. It is only a shallow copy that doesn't reference the same object: \n")
lis2 = lis[:]
print(lis2)
print(lis2 is lis)
print(lis2 == lis)
print("\n")

# Use "del" to delete an element from a list, tuple or dict(by key)
print("'del' can be used to delete an element from a list: \n")
del lis2[2]
print(lis2)
print("\n")

# Lists can be either added or concatenated
# Adding list + list -> new_list
# Concatenating list.extend(list) -> void (updates the first list)
print("Lists can be added or concatenated (+ or .extend): \n")
letters = ['hi']
print(lis2 + letters)
lis2.extend(letters)
print(lis2)
print("\n")

# "in" can be used to check for a value existing in a list, tuple, dict(keys) and set
print("'in' can be used to check for a value in a list, tuple, dict(keys) and set: \n")
print('hi' in lis)
print(1 in lis2)
print("\n")

# Typles are like lists but with immutability
print("Tuples are like lists but they are immutable: \n")
tup = (1,  2, 3)
print(tup)
print("\n")

# Tuples with one value have to have a "," after the item
print("Tuples with 1 value need a comma otherwise they return the value: \n")
print((1,))
print((1))
print(())
print("\n")

# Most list operations work the same
print("Most of the list operations can be used the same: \n")
print(len(tup))
print(tup + (4, 5, 6))
print(tup[:2])
print(1 in tup)
print("\n")

# Tuples and lists can be destructured
print("Tuples and lists can be destructured into variables: \n")
a, b, c = tup
print(a, b, c)
a, *b, c = tup + (4, 5, 6)
print(a, b, c)
print("\n")

# Keys for dictionaries have to be immutable types. (e.g int, float, string, tuple)
print("Keys for dicts need to be immutable (e.g. int, float, string, tuple): \n")
dict = { "one" : 1, 2: "two", 3.0: 3}
print(dict)
print("\n")

# Sets can be created in two ways
print("Sets are created in two ways: \n")
st = set()
st2 = {1, 2, 3, 4, 5}
print(st)
print(st2)
print("\n")

# Set elements need to be immutable
print("Set elements need to be immutable: \n")
st.add(1)
st.add('hi')
st.add((1))
print(st)
print("\n")

# Set elements cannot be repeated
print("Set elements cannot be duplicates: \n")
st.add(1)
print(st)
print("\n")

# Set intersection is done with &
# This will find all same values
print("Sets intersection is done witht &: \n")
print(st & st2)
print("\n")

# Set union is handled with |
print("Sets are combined (union) via |: \n")
print(st | st2)
print("\n")

# Set difference uses -
# Finds the values that differ from each set
# Does not include values from the second set that differs
print("Set differences uses -: \n")
print(st2 - st)
print("\n")

# Set symmetric difference uses ^
# Will find differences from both sets
print("Set symmetric difference uses ^: \n")
print(st2 ^ st)
print("\n")

# Find a set superset with >=
# If the first set is contained within the second set
print("Fine if a set is a superset of another set with >=: \n")
print(st >= st2)
print("\n")

# Find if a set is a subset of another with <=
# If the second set is contained within the first
print("Find if a set is a subset of another with <=: \n")
print(st <= st2)
print("\n")

# try, except, else, finally
# Handles catching errors and finalising a process
# pass is used to noop
print("try, except, else, finally: \n")
try:
    raise IndexError("I am an error")
except IndexError as e:
    print('Index Error')
    pass
except (TypeError, NameError):
    print("Multiple handled exceptions")
    pass
else:
    # Runs if no exceptions fire
    print("All fine")
finally:
    # Will always run
    print('Finally block')
print("\n")

# "with" can be used to handle exceptions in a terser way than "try"
# Useful with opening files as it will handle closing (same with streams)
# Can also be used to write to files, streams, etc
print("'with' is used to handle opening files, streams, etc in a terser way (than using 'try'): \n")
with open('test.txt', 'w+') as file:
    file.write("konnichiwa")
with open('test.txt') as file:
    for line in file:
        print(line)
print("\n")

# Iterable objects are generics that act like lists
print("Iterable objects are generics that act as lists: \n")
a_dict = {1: 'one', 2: 'two', 3: 'three'}
print(a_dict.keys()) # Iterable created
for i in a_dict.keys():
    print(i)
print("\n")

# An iterable can be pulled out into an actual list with 'list'
print("An iterable can be pulled out into an actual list with 'list': \n")
dict_list = list(a_dict.keys())
print(dict_list)
print("\n")

# Functions are defined with def
print("Functions are defined with 'def': \n")
def a_func():
    print("I'm a function")
    return 'banana'
print(a_func())
print("\n")

# Functions have have named or non-named parameters
print("Functions have named or non-named parameters: \n")
def b_func(a, b):
    return a + b
print(b_func(1, 2))
print(b_func(a=2, b=3))
print("\n")

# Variable number of keyword and non keyword args can be used
print("A varable number of keyword and non-keyword arguments can be used: \n")
def c_func(*args):
    return args
def d_func(**kwargs):
    return kwargs
def e_func(*args, **kwargs):
    print(args)
    print(kwargs)
print(c_func(1, 2, 3))
print(d_func(a=1, b=2, c=3))
e_func(
    1, 2,
    a=3, b=4
)
print("\n")

# Variables can be expanded into a function
# Keys for kwarsg must be strings
print("Variables can be expanded into a function: \n")
e_func(
    *(1, 3, 4, 5),
    **{'one': 1, 'two': 2}
)
print("\n")

# Multiple values can be returned as a tuple
print("Multiple values can be returned as a tuple: \n")
def f_func(a, b):
    return b, a # or (b, a)
print(f_func(1, 2))
x = 1
y = 2
print(x, y)
x, y = f_func(x, y)
print(x, y)
print("\n")

# A global variable can be used inside a function with the 'global' keyword
print("A global variable can be used inside a function with the 'global' keyword: \n")
x = 1
def g_func(n):
    global x
    print(x)
    x = n
    print(x)
g_func(5)
print("\n")

# Anonymous functions are lambdas
print("Anonymous functions are lambdas: \n")
print((lambda x: x > 2)(3))
print((lambda x, y: x ** 2 + y ** 2)(2, 3))
print("\n")

# List comprehensions are shorthand list modifications
# Handy for mapping and filtering
# The output is a list so these can be nested
print("List comprehensions are shortrhand list modifications: \n")
# Mapping
def add_10(n):
    return n + 10
x = [add_10(i) for i in [1, 2, 3]]
print(x)
x = [(lambda x: x + 10)(i) for i in [1, 2, 3]]
print(x)
x = [x + 10 for x in [1, 2, 3]]
print(x)
# Filtering
x = [x for x in [1, 2, 3] if x > 1]
print(x)
print("\n")

# Dict & set comprehensions are shorthand modifications
print("Dict & set comprehensions are shorthand modifications: \n")
# Sets
x = {x for x in 'abcdddddeeeeff' if x not in 'abc'}
print(x)
# Dict
x = {x: x ** 2 for x in range(5)} # x is the key and then the value is x to the power of 2
print(x)
print("\n")