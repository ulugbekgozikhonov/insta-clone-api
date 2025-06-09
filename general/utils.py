EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUMBER_REGEX = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

import re  # noqa: E402

def is_valid_email(email):
    """
    Validate the email address using a regex pattern.
    """
    return re.match(EMAIL_REGEX, email) is not None

def is_valid_phone_number(phone_number):
    """
    Validate the phone number using a regex pattern.
    """
    return re.match(PHONE_NUMBER_REGEX, phone_number) is not None

if __name__ == "__main__":
    # Example usage
    print(is_valid_email("test@example.com"))
    print(is_valid_phone_number("+998994567890"))