# VSCode Debugger Activities
***
## Debug Log

``` python
def calculate_total(price, quantity):
    total = price * quantity  # Line 3
    return total  # Line 4

def apply_discount(total, discount):
    return total - (total * discount / 100)  # Line 6 
# - The discount is not calculated using a percentage but rather as a whole number

def main():
    price = 100
    quantity = 5
    discount = 10  #
    total = calculate_total(price, quantity)  # Line 10
    total_after_discount = apply_discount(total, discount)  # Line 11 
# - Did not access the discount parameter in the function while calling it
    print(f"Total after discount: {total_after_discount}")  # Line 12

main()

```
- Answer: The first error I encountered while using the debugger and single line stepping was the fact that the discount parameter used in the original apply_discount function was not being accessed, furthermore leading to the primary error. While the program was working however, I checked variable values upon the discount and realised that it was not being initialised as a percentage, leading to the program calculating the discounted price as -4500, which is not possible. I fixed this issue through dividing the discount in the function by 100 and then multiplying it with the total, and subtracting it from the whole total, giving us the total after discount to be 450.