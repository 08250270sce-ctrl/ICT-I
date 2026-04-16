i=10
while i>=1:
    print(i)
    i-=1
print("Times up!")

i=0
while True:
    number=int(input("Enter an integer(0 to stop): "))
    if number==0:
        break
    i+=number
print("Total Sum:",i)

#question 3
correct_username = "admin"
correct_password = "1234"

i = 3

while i > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("login successful")
        break
    else:
        i -= 1
        if i > 0:
            print(f"Incorrect. You have {i} attempt(s) left.")
        else:
            print("account locked")