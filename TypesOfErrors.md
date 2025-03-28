# Types of Errors Activities
***

### - What error is used in the following programs? Explain what is wrong with each.

``` python

def calculate_area(radius):
    area = 3.14 x radius x 2
    return area

print(calculate_area(5))
print(calculate_area(3))

```

- Answer: The following program has a SyntaxError, due to the invalid units utilised in the program, specifically the x symbol trying to be used for times, however we have to use * instead in python.

``` python
def calculate_area(length, width):
    return length + width

area = calculate_area(5, 3)
print(f"Area: {area}")

```
- Answer: The following program has to calculate area, however the program calculates with a + symbol instead of a * symbol, presenting a logical error.

``` python
def divide(a, b):
    return a / b

result = divide(10, 0)
print(result)

```

- Answer: This error is the DivisionByZero Error, however it coincides into the error associated with while the program is running, being the runtime error.

``` python
for i in range(5)
    print(i)

```

- Answer: This error circulates around a Syntax Error, due to not including a colon (:) after a conditional statement or loop.

``` python
def calculate_average(numbers):
    total = sum(numbers)
    return total - len(numbers)

numbers = [10, 20, 30, 40]
average = calculate_average(numbers)
print(f"Average: {average}")

```

- Answer: This error is a logical error, where instead of dividing when calculating the average the program is subtracting.

``` python
def calculate_area(diameter):
    return math.pi * diameter ** 2

print(calculate_area(5))

```
- Answer: Instead of calculating the area of a circle with math.pi * radius ** 2, the program is calculating with the parameter/variable diameter.
