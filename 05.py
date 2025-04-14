def main():
    # Prompt user for side lengths
    try:
        # Get length of side 1
        side1 = float(input("What is the length of side 1? "))
        
        # Get length of side 2
        side2 = float(input("What is the length of side 2? "))
        
        # Get length of side 3
        side3 = float(input("What is the length of side 3? "))
        
        # Calculate perimeter
        perimeter = side1 + side2 + side3
        
        # Print the perimeter
        print(f"The perimeter of the triangle is {perimeter}")
    
    except ValueError:
        print("Error: Please enter valid numbers for side lengths.")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()