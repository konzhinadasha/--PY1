import random
import string

def get_random_password() -> str:
    length = 8
    letters = string.ascii_uppercase + string.ascii_lowercase
    numbers = string.digits
    password_items = letters + numbers
    return ''.join(random.sample(password_items, length, counts=None))



print(get_random_password())
