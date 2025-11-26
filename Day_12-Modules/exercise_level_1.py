from random import choice
from string import ascii_letters, digits

def random_user_id(length=6) -> str:
    characters = ascii_letters + digits
    gen = ''.join(choice(characters) for i in range(length))
    return gen

