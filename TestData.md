# Test Data Activities
***
## Question 1
### - Compare boundary testing, path coverage testing and faulty and abnormal data testing.

- A: Boundary value testing is a technique used to identify errors at the boundaries of input ranges. This is usally used for functions with integer related instances, essentially checking inputs between number boundaries. For instance, if a program accepts numbers between 1 - 100, and slightly beyond or less the valid limits, it helps uncover issues that may not be evident when testing within the original range of inputs. Path coverage on the other hand, is a technique vital for identifying logical errors, specifically circulated around if, and else statement programs. An example includes checking the discount of a person based on age. If the age is below 18, return the child discount, else if the age is greater than or equal to 65, return the senior discount. Notice how an instance where between 18 and 65, nothing is outputted. We can replace this test case with, no discount, ensuring that all the possible execution paths are tested throughout the program. Another type of testing method utilised is faulty and abnormal data testing. This is used to evaluate how well a program handles invalid or unexpected inputs. We may ask the program to enter an integer, but the user may input a string, leading to the program returning an error message. In this instance, we can ensure that the program doesn't output this by creating test cases, instead of displaying an error message and instead requesting a valid input of an integer. Furthermore, we can conclude that boundary value testing is utilised for boundaries of input ranges, path coverage is utilised for logical errors and conditions, and faulty and abnormal data testing is used for handling invalid or unexpected data inputs.

## Question 2

### - Write test cases for boundary values for the following:

``` python
def is_safe_temperature(temp):
    return 0 <= temp <= 100

# TODO: Write test cases for boundary values
print(is_safe_temperature(-1)) # Boundary Case (Below Valid)
print(is_safe_temperature(0)) # Lower Boundary
print(is_safe_temperature(100)) # Upper Boundary
print(is_safe_temperature(101)) # Boundary Case (Above Valid)
```
## Question 3

### - Write test cases for path coverage for the following:

``` python
def ticket_price(age):
    if age < 5:
        return "Free"
    elif 5 <= age <= 17:
        return "$5"
    elif 18 <= age <= 64:
        return "$10"
    else:
        return "Senior Discount - $7"

# TODO: Write test cases for all paths
print(ticket_price(4)) # Free (Path 1)
print(ticket_price(5)) # 5$ (Path 2)
print(ticket_price(18)) # $10 (Path 3)
print(ticket_price(65)) # Senior Discount - $7 (Path 4)
```

## Question 4

### - Write test cases for faulty and abnormal data for the following:

``` python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input, numbers required"

# TODO: Write test cases for abnormal and faulty inputs
print(divide_numbers(10, 0))
print(divide_numbers('5', 1))
```