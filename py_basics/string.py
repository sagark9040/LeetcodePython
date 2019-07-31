x = 'Coke'
y = 'Pepsi'
z = 'Sprite'

#concatenate
print (x + ' & ' + y + ' & ' + z)

#repeat
print ("repeat coke: ", x*2)

#slicing .. substring from position
sub1 = x[2:]
print(sub1)

#slicing .. substring from and to
sub_from_to = x[1:3]
print(x, "1:3", sub_from_to)

# Slicing .. string.charAt
char_at = y[0] + y[1]
print(char_at)

#reverse a string
s = 'sAGARnambi'
print(s[::-1])
print(s[::2], '..', s[1::-2])

#capitalize
print("orig:", s)
s = str.upper(s)
print("upper:", s)
s = str.lower(s)
print("lower:", s)
s = s.replace("sagar", "new")
print(s)