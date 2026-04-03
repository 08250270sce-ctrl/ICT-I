userDetails={'Id':1,'userName':'Just_me'}
print(type(userDetails))
print(userDetails)

location=dict(s='Samtse',t='Thimphu',p='Paro')
print(location)

#Accessing values from the dictionary using keys
print(userDetails['userName'])#Output: Just_me
print(location.get('t'))#Output: Thimphu

#new Item are added to the dictionary using assignment operator
userDetails['email']='justme@example.com'#Adding new key-value pair to the dictionary
print(userDetails)#Output: {'Id': 1, 'userName': 'Just_me', 'email': 'justme@example.com'}
userDetails['userName']='Just_me_updated'#Updating the value of an existing key
print(userDetails)#Output: {'Id': 1, 'userName': 'Just_me_updated', 'email': 'justme@example.com'}

del location['p']#Removing a key-value pair from the dictionary using del keyword
print(location)#Output: {'s': 'Samtse', 't': 'Thimphu'}

deleted_vale=userDetails.pop('email')#Removing a key-value pair using pop method and storing the removed value in a variable
print(deleted_vale)#Output:

del_key,del_value=userDetails.popitem()#Removing the last inserted key-value pair using popitem method and storing the removed key and value in separate variables
print(f'the deleted key is {del_key}and the deleted value is {del_value}')
location.clear()#Removing all key-value pairs from the dictionary using clear method
print(location)#Output: {}