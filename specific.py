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

# "in" can be used to check for a value existing in a list, tuple or dict(keys)
print("'in' can be used to check for a value in a list: \n")
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

#