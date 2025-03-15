import math

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(start, end):
    """Calculate the sum of all prime numbers in a given range."""
    return sum(num for num in range(start, end + 1) if is_prime(num))

def length_converter(value, direction):
    """Convert length between meters and feet."""
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif direction.upper() == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
        raise ValueError("Invalid direction. Use 'M' for meters to feet or 'F' for feet to meters.")

def consonant_count(text):
    """Count the number of consonants in a given string."""
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

def min_max_finder(numbers):
    """Find the minimum and maximum numbers from a list."""
    if not numbers:
        raise ValueError("No numbers provided.")
    return min(numbers), max(numbers)

def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def main():
    while True:
        print("\nMenu:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Consonant Counter")
        print("4. Min-Max Number Finder")
        print("5. Palindrome Checker")
        print("6. Exit")

        choice = input("Select a function (1-6): ")

        if choice == '1':
            try:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                result = prime_sum(start, end)
                print(f"Sum of prime numbers between {start} and {end} is: {result}")
            except ValueError:
                print("Invalid input. Please enter integers.")

        elif choice == '2':
            try:
                value = float(input("Enter the length value: "))
                direction = input("Enter conversion direction (M/F): ")
                result = length_converter(value, direction)
                print(f"Converted length: {result}")
            except ValueError as e:
                print(e)

        elif choice == '3':
            text = input("Enter a text string: ")
            result = consonant_count(text)
            print(f"Number of consonants: {result}")

        elif choice == '4':
            try:
                numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                smallest, largest = min_max_finder(numbers)
                print(f"Smallest: {smallest}, Largest: {largest}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            text = input("Enter a text string: ")
            result = is_palindrome(text)
            print(f"Is the string a palindrome? {result}")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")

if __name__ == "__main__":
    main()

