def reverse_integer(x):
    """
    Reverse digits of a 32-bit signed integer.
    
    Args:
    x (int): The input 32-bit signed integer.
    
    Returns:
    int: The reversed integer, or 0 if it overflows.
    """
    # Define the 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Determine the sign of the number
    sign = -1 if x < 0 else 1
    
    # Reverse the digits of the absolute value of x
    reversed_num = int(str(abs(x))[::-1])
    
    # Apply the sign and check for overflow
    result = sign * reversed_num
    if result < INT_MIN or result > INT_MAX:
        return 0
    
    return result

# Loop for multiple inputs
while True:
    try:
        user_input = input("Enter a 32-bit signed integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        user_input = int(user_input)  # Convert input to integer
        output = reverse_integer(user_input)
        print("Reversed Output:", output)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
