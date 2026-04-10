tup=("John Smith","Jane Doe","Alice Johnson")
for x in tup:
    print(x)

set1={10,30,20}
for x in set1:
    print(x)

bookdetails=dict({"Python Programming":"John Smith","Python Fundamentals":"Alice Johnson","Python Interview Question":"Jane Doe"})
for key in bookdetails:# key is the variable that takes the value of each key in the dictionary.
    print(key, bookdetails[key])
