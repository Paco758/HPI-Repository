# TEST GIST FOR THE SUBJECT HPI (2024)

# MIT License
# 
# Copyright (c) 2024 Autonomous Cars
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Function to calculate the sum of two numbers
def calculate_sum(base_number1, base_number2):
    # Set the numbers to calculate the sum of
    hypothetical_number1 = base_number1
    hypothetical_number2 = base_number2
    # Calculate the substraction of the two numbers
    hypothetical_sum = hypothetical_number1 + hypothetical_number2
    return hypothetical_sum

# Function to calculate the substraction of two numbers
def calculate_substraction(base_number1, base_number2):
    # Set the numbers to calculate the substraction of
    hypothetical_number1 = base_number1
    hypothetical_number2 = base_number2
    # Calculate the substraction of the two numbers
    hypothetical_substraction = hypothetical_number1 - hypothetical_number2
    return hypothetical_substraction

# Function to calculate the multiplication of two numbers
def calculate_multiplication(base_number1, base_number2):
    # Set the numbers to calculate the multiplication of
    hypothetical_number1 = base_number1
    hypothetical_number2 = base_number2
    # Calculate the multiplication of the two numbers
    hypothetical_multiplication = hypothetical_number1 * hypothetical_number2
    return hypothetical_multiplication

# Function to calculate the division of two numbers
def calculate_division(base_number1, base_number2):
    # Set the numbers to calculate the division of
    hypothetical_number1 = base_number1
    hypothetical_number2 = base_number2
    hypothetical_division = []
    # Calculate the division of the two numbers
    hypothetical_division.append(hypothetical_number1/hypothetical_number2)
    hypothetical_division.append(hypothetical_number1%hypothetical_number2)
    return hypothetical_division

# Function to calculate the exponentiation of two numbers
def calculate_exponentiation(base_number, base_exponent):
    # Set the numbers to calculate the division of
    hypothetical_number = base_number
    hypothetical_exponent = base_exponent
    # Calculate the exponent of the number
    hypothetical_exponentiation = hypothetical_number ** hypothetical_exponent
    return hypothetical_exponentiation

# Function to calculate a factorial based on a number
def calculate_factorial(base_number):
    hypothetical_number = 0
    # Check if the number can be calculated as a factorial
    # Factorial of a negative can't be calculated, return an error message
    if base_number < 0:
        return None
    # Factorial of zero is 1, return 1
    elif base_number == 0:
        hypothetical_factorial = 1
        return hypothetical_factorial
    # Calculate the factorial of the number given
    else:
        hypothetical_factorial = 1
        # Calculate the factorial looping and increasing the numbers
        for i in range(1, base_number + 1):
            hypothetical_factorial *= i
        return hypothetical_factorial
            

if __name__ == "__main__":
    # Ask for the operation that  the user wants to use
    operation = str(input("What operation do you want to make (SUM, SUBS, MULT," 
                      " DIVIS, EXP, FACT): "))
    if operation == "SUM":
        # Ask for the numbers that should calculate the sum of
        number1 = float(input("Insert a number to calculate the sum: "))
        number2 = float(input("Insert another number to calculate the sum: "))
        sum12 = calculate_sum(number1, number2)
        
        # Show a message with the original numbers and the result
        print("The sum of", number1, "and", number2, "is", sum12)
    
    elif operation == "SUBS":
        # Ask for the numbers that should calculate the substraction of
        number1 = float(input("Insert a number to calculate the "
                              "substraction: "))
        number2 = float(input("Insert another number to calculate the "
                            "substraction: "))
        subs12 = calculate_substraction(number1, number2)
        
        # Show a message with the original numbers and the result
        print("The substraction of", number1, "and", number2, "is", subs12)
    
    elif operation == "MULT":
        # Ask for the numbers that should calculate the multiplication of
        number1 = float(input("Insert a number to calculate the "
                              "multiplication: "))
        number2 = float(input("Insert another number to calculate the "
                              "multiplication: "))
        mult12 = calculate_multiplication(number1, number2)
        
        # Show a message with the original numbers and the result
        print("The multiplication of", number1, "and", number2, "is", mult12)
    
    elif operation == "DIVIS":
        # Ask for the numbers that should calculate the division of
        number1 = float(input("Insert a number to calculate the "
                              "division: "))
        number2 = float(input("Insert another number to calculate the "
                              "division: "))
        # Check if the division could be calculated
        if number2 == 0:
            print("Numbers can't be divided by zero.")
        else:
            divd12 = calculate_division(number1, number2)[0]
            rest12 = calculate_division(number1, number2)[1]
            # Show a message with the original numbers and the result
            print("The division of", number1, "and", number2, "is", divd12,
              ", with a rest of", rest12)
    
    elif operation == "EXP":
        # Ask for the number that should calculate the exponentiation  of
        # and the exponent
        number = float(input("Insert a number to calculate the "
                              "exponentiation: "))
        exponent = float(input("Insert the exponent: "))
        exponentiation = calculate_exponentiation(number, exponent)
        
        # Show a message with the original numbers and the result
        print(number,"to the power of", exponent, "is", exponentiation)
    
    elif operation == "FACT":
        # Ask for the number that should calculate the factorial of
        number = int(input("Insert a number to calculate the factorial: "))
        factorial = calculate_factorial(number)
        # Check if the factorial could be calculated
        if factorial == None:
            print("Number it's out of range.")
        # Show a message with the original number and the result
        else:
            print("The factorial of", number, "is", factorial)

