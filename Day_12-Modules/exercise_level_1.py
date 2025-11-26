from random import choice
from string import ascii_letters, digits

def random_user_id(length=6) -> str:
    characters = ascii_letters + digits
    gen = ''.join(choice(characters) for i in range(length))
    return gen



def user_id_gen_by_user() -> str:
    length1 = int(input("length of id: "))
    length2 = int(input("number of id(s): "))

    acc = []
    for i in range(length2):
        acc.append(random_user_id(length1))

    return acc

print(user_id_gen_by_user())
    