name = input("enter your name: ")
borrowed_book = int(input("enter the number of days the book was borrowed: "))
returned_book = int(input("enter the number of days late the book was returned: "))
print(f"hello {name} you borrowed the book for {borrowed_book} days and returned it {returned_book} days late")

if returned_book == 0 :
    print("thank you for returning the book on time")
elif returned_book > 0 and returned_book <= 5:
    fine = 5 * returned_book
    print(f"you have to pay a fine of nu.{fine} ")
elif returned_book == 6 and returned_book <=10:
    fine = 10 * returned_book 
    print(f"you have to pay a fine of nu.{fine} ")  
elif returned_book > 10:
    fine = 20 * returned_book
    print(f"you have to pay a fine of nu.{fine} ")  

else:
    print("warning you have to return the book as soon as possible or your library privilages will be restricted    ")

if borrowed_book > 30:
    print("Warning: You have borrowed the book for too long. Please return it as soon as possible or your library privileges will be restricted.")