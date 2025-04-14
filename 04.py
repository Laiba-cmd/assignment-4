def main():
    # Anton's age is given
    anton_age = 21

    # Calculate Beth's age (8 years older than Anton)
    beth_age = anton_age + 8

    # Calculate Chen's age (25 years older than Beth)
    chen_age = beth_age + 25

    # Drew's age is Chen's age plus Anton's age
    drew_age = chen_age + anton_age

    # Ethan's age is the same as Chen's
    ethan_age = chen_age

    # Print out the names and ages
    print("Anton: " + str(anton_age))
    print("Beth: " + str(beth_age))
    print("Chen: " + str(chen_age))
    print("Drew: " + str(drew_age))
    print("Ethan: " + str(ethan_age))

# Ensure the script can be run directly
if __name__ == "__main__":
    main()