# Python Debugger Activities
***
## Question 1
### - Run the above code. When the debugger starts running, type 'n' and press enter on each line until you are finished debugging. Describe what happened.

- Answer: The execution finishes and the python debugger starts, and as you type 'n' perpetually, the debugger first initialises the price variable as 100, next quantity = 5, discount = 0.1 or a 10% discount, it initialises the function to calculate the total and create the total variable with the price and quantity given, after it will apply the discount on the total and finally print the total after the discount. This is if I move the pause function above and to the start of the main function, however if I keep it at the end then it will directly skip to the total after discount print.

***
## Question 2 and 3
### - Run the above code. When the debugger starts running, type 's' and press enter on each line until you are finished debugging. Describe what happened. Compare the 's' and 'n' command.

- Answer: This time, the program runs in single line stepping, allowing me to see each line of the code, being the exact same output as before if I move the pause function (Sorry didn't mean to) But overall 'n' caused it to skip the entire function call and 's' caused it to go through each line in the function.

***
## Question 4 and 5
### - Run the above code. When the debugger starts running, type 's' and press enter for 8 lines in a row. Then, type 'whatis total'. Then, type 'p total'. Describe what happened. Compare the whatis and print(p) command.

- Answer: The code does single line stepping until the calculate_total function, where it calls this function, then it returns the total. I then ask for the type of variable of total with the whatis command, giving the class 'int', and after use the p total command, giving me the value of total, which is 500. The whatis command gives me the class of the variable, whereas the p total gives the me the message/value in the variable total.