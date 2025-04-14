def main():
    # Prompt user to enter a number
    try:
        # Get number from user input
        number = float(input("Type a number to see its square: "))
        
        # Calculate the square
        square = number * number
        
        # Print the result
        print(f"{number} squared is {square}")
    
    except ValueError:
        print("Error: Please enter a valid number.")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()