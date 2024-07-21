import re

# Function to validate email addresses
def validate_email(email):
    """
    Validate the email address using regex.
    :param email: str - Email address to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.±]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$'
    # pattern = r'^(?:(?!.*?[.]{2})[a-zA-Z0-9](?:[a-zA-Z0-9.+!%-]{1,64}|)|\"[a-zA-Z0-9.+!% -]{1,64}\")@[a-zA-Z0-9][a-zA-Z0-9.-]+(.[a-z]{2,}|.[0-9]{1,})$'
    # Use re.match to check if the email matches the pattern
    return bool(re.match(pattern, email))


# Function to validate phone numbers
def validate_phone(phone):
    """
    Validate the phone number using regex.
    :param phone: str - Phone number to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid phone number
    pattern = r'^\+359[1-9][0-9]{7,8}$'
    # Use re.match to check if the phone matches the pattern
    return bool(re.match(pattern, phone))


# Function to validate postal codes
def validate_postal_code(postal_code):
    """
    Validate the postal code using regex.
    :param postal_code: str - Postal code to validate
    :return: bool - True if valid, False otherwise
    """
    # Define the regex pattern for a valid postal code
    pattern = r'^\d{4}$'
    # Use re.match to check if the postal code matches the pattern
    return bool(re.match(pattern, postal_code))


def main():
    """
    Main function to get user input and validate using the defined functions.
    """
    # Get email input from the user
    email = input('Enter your email address: ')
    # Validate the email and print the result
    if validate_email(email):
        print('The email address is valid.')
    else:
        print('The email address is invalid.')

    # Get phone number input from the user
    phone = input('Enter your phone number (XXX-XXX-XXXX): ')
    # Validate the phone number and print the result
    if validate_phone(phone):
        print('The phone number is valid.')
    else:
        print('The phone number is invalid.')

    # Get postal code input from the user
    postal_code = input('Enter your postal code (XXXXX or XXXXX-XXXX): ')
    # Validate the postal code and print the result
    if validate_postal_code(postal_code):
        print('The postal code is valid.')
    else:
        print('The postal code is invalid.')


# Call the main function
if __name__ == '__main__':
    main()