numbers_str = input("Enter numbers separated by spaces: ")
numbers_list = [int(num) for num in numbers_str.split()]

even_numbers = []
odd_numbers = []

for number in numbers_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)