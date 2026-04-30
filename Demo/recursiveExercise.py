def print_pattern(n):
    if n == 1:   # base case
        print("*")
        return
    
    print_pattern(n - 1)   # recursive call with smaller value
    
    # print stars after returning from recursion
    for i in range(n):
        print("*", end=" ")
    print()


# Example
print_pattern(4)