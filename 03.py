def main():
    # Prompt the user to enter temperature in Fahrenheit
    fahrenheit_str = input("Enter temperature in Fahrenheit: ")
    
    # Convert input to float
    try:
        degrees_fahrenheit = float(fahrenheit_str)
        
        # Convert Fahrenheit to Celsius using the given equation
        degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
        
        # Print the result, showing both Fahrenheit and Celsius
        print(f"Temperature: {fahrenheit_str}F = {degrees_celsius}C")
    
    except ValueError:
        print("Error: Please enter a valid number for temperature.")

# Ensure the script can be run directly
if __name__ == "__main__":
    main()