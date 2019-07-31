
tuple = (1,2,3)
l = [1, 2, 3]
print(tuple)
print(l)

print(tuple[1])
print(l[1])
l = list(range(1, 1001))
print("rng[2]", l[2])

#
a = [[[i,j] for j in range (5)] for i in range (5)]

for x in range(len(a)):
    for y in range(len(a[0])):
        print(a[x][y], end="")
    print("\n")


# Tuples are fixed size in nature whereas lists are dynamic.
# In other words, a tuple is immutable whereas a list is mutable.
#
# You can't add elements to a tuple. Tuples have no append or extend method.
# You can't remove elements from a tuple. Tuples have no remove or pop method.
# You can find elements in a tuple, since this doesn’t change the tuple.
# You can also use the in operator to check if an element exists in the tuple.
# Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to
# do with it is iterate through it, use a tuple instead of a list.
#
# It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a
# list is like having an implied assert statement that this data is constant, and that special
# thought (and a specific function) is required to override that.
#
# Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like
# strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.


l = ['a', 'b', 'c', 1234]
sp = l[::-1]
print ("splice:", sp)

l.append("last")
print(l)

l.remove('a')
print('list without a:', l)