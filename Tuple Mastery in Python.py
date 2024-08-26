# Task 1: Formatting Flight Itineraries

# Function to format flight itineraries
def format_itineraries(itineraries):
    """
    This function takes a list of tuples as an argument.
    Each tuple contains information about a flight itinerary: (traveler_name, origin, destination).
    The function returns a formatted string that lists each itinerary.
    """
    formatted_itineraries = []
    for i, itinerary in enumerate(itineraries, start=1):
        traveler_name, origin, destination = itinerary
        formatted_itineraries.append(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")
    return "\n".join(formatted_itineraries)

# Function to get user input for itineraries
def get_user_input():
    """
    This function prompts the user to input traveler names, origins, and destinations.
    It returns a list of tuples containing the input data.
    """
    itineraries = []
    while True:
        traveler_name = input("Enter traveler name (or 'done' to finish): ")
        if traveler_name.lower() == 'done':
            break
        origin = input("Enter origin: ")
        destination = input("Enter destination: ")
        itineraries.append((traveler_name, origin, destination))
    return itineraries

# Main function to run the program
def main():
    """
    Main function to run the program.
    It gets user input, formats the itineraries, and prints the formatted string.
    """
    itineraries = get_user_input()
    formatted_string = format_itineraries(itineraries)
    print("\nFormatted Itineraries:\n")
    print(formatted_string)

# Run the main function
if __name__ == "__main__":
    main()
