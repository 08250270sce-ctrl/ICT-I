greetings = open("hello.txt","r")
print(greetings)

#close() function method closes the file and  releases the system resources.
#closing ensures that all changes are properly svaed
greetings.close()
f=open("hello.txt","r")
print("filename",f.name)
print("file mode:",f.mode)
print("Is file closed?:",f.closed)
f.close()
print("Is file closed?:",f.closed)

#reading file
f=open("hello.txt","r")
contents=f.read()
print(contents)
f.close()

#writing a file
newFile=open("newFile.txt","w")
print(newFile)

newFile.write("This is a new file created by python.")
newFile.close()

FileOverwrite=open("newFile.txt","w")
FileOverwrite.write("This contents of the newFile is now changed.")
FileOverwrite.close()

#append a file
appendFile=open("hello.txt","a")
appendFile.write("\n\nDon't forget to smile today")
appendFile.close()

#with Statement
with open("hello.txt","r") as f:
    contents=f.read()
    print(contents)