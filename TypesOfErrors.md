# Testing the System Activities
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

