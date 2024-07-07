from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """Calculates the future date by adding a specified number of days to the current date."""
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    try:
        # Prompt the user to enter a number of days
        days_input = input("Enter the number of days to add to the current date: ")
        days_to_add = int(days_input)
        
        # Calculate and display the future date
        calculate_future_date(current_date, days_to_add)
    
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

if __name__ == "__main__":
    main()