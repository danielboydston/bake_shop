import re
# project utilities

def phone_to_storage(phone: str):
    """Converts a phone number string to only numbers for storage in a database"""
    cleaned = re.sub(r'[^\d]', '', phone)
    if len(cleaned) not in [10,11]:
        return False
    
    return cleaned

def phone_to_display(phone: str):
    """Converts a phone number without punctuation to a more human readable string"""

    pattern = r'([01]?)(\d{3})(\d{3})(\d{4})'

    output = ''
    match = re.search(pattern, phone)
    if match:

        if match.group(1) == '0':
            output = match.group(1)
        elif match.group(1) == '1':
            output = f"{match.group(1)}-"
        
        output = f"{output}{match.group(2)}-{match.group(3)}-{match.group(4)}"
    else:
        output = phone

    return output