def calculate_lucky_number():
    """
    This script greets the user and calculates a "lucky number"
    based on their favorite number input.
    """
    # Get user's name with validation
    while True:
        user_name = input("Hello! What's your name? ").strip()
        if user_name:
            break
        print("Please enter a valid name!")
    
    print(f"Nice to meet you, {user_name}!")
    
    # Get user's favorite number with validation
    while True:
        try:
            favorite_number = input("What's your favorite number? ")
            favorite_number = int(favorite_number)
            break
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nGoodbye! Have a great day!")
            return
    
    # Calculate lucky number
    lucky_number = favorite_number * 2
    
    print(f"Your lucky number is: {lucky_number}")
    print("Have a great day!")

if __name__ == "__main__":
    calculate_lucky_number()




