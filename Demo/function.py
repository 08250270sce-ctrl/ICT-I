print()
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3
def calculate_average(total):
    return total / 3
def result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
total = calculate_total(m1, m2, m3)
average = calculate_average(total)
final_result = result(average)
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", final_result)
num = int(input("Enter a number to check even/odd: "))
print("The number is:", check_even_odd(num))
print()