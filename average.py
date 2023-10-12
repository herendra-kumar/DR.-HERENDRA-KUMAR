def find_average(numbers):
total = 0
count = 0
for number in numbers:
total += number
count += 1
return total / count
# Test the function
numbers = [1, 2, 3, 4, 5]
average = find_average(numbers)
print(average)