my_tuple=('Hello',123456)
print(type(my_tuple))
print(my_tuple)#Output: ('Hello', 123456)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[-1])#Output: Hello
a, b=my_tuple
print(b)#Output: 123456
new_tup=tuple(a)#covert strin 'hello' to tuple of characters
print(new_tup)#Output: ('H', 'e', 'l', 'l', 'o')
concatenated_tuple= my_tuple+new_tup
print(concatenated_tuple)#Output: ('Hello', 123456, 'H', 'e', 'l', 'l', 'o')
print(concatenated_tuple[2:6:2])#Output: ('H', 'l')
print(concatenated_tuple[::-1])#Output: ('o', 'l', 'l', 'e', 'H', 123456, 'Hello')

print(concatenated_tuple[6:1:-4])





