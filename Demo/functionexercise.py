print()
def calculate_total(x,y,z):
    return x+y+z

def calculate_average(total):
    return total/3

x = float(input("Enter marks for subject 1: "))
y = float(input("Enter marks for subject 2: "))
z = float(input("Enter marks for subject 3: "))

total = calculate_total(x, y, z)
average = calculate_average(total)

print("Total Marks:", total)
print("Average:", average)
if average>=50:
    print("Result: Pass")
else:
    print("Result: Fail")
print()
    