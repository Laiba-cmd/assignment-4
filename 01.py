def main():
    # Prompt the user to enter the first number
    #print("Sum Calculator")
    #print("-------------")
    
    # First number input
    first_number_str = input("Please enter the first number: ")
    
    # Convert first input to integer
    try:
        first_number = int(first_number_str)
    except ValueError:
        print("Error: Please enter a valid integer for the first number.")
        return
    
    # Second number input
    second_number_str = input("Please enter the second number: ")
    
    # Convert second input to integer
    try:
        second_number = int(second_number_str)
    except ValueError:
        print("Error: Please enter a valid integer for the second number.")
        return
    
    # Calculate the sum
    total_sum = first_number + second_number
    
    # Print the result
    print(f"\nResult: {first_number} + {second_number} = {total_sum}")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    main()