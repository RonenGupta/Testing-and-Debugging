def calculate_average(numbers):
    total = sum(numbers)
    return total - len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")