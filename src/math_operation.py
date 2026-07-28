def add_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtracts the second number from the first number.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The difference of the two numbers.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiplies two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The product of the two numbers.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divides the first number by the second number.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The quotient of the two numbers.

    Raises:
    ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("The second number cannot be zero.")
    return a / b
