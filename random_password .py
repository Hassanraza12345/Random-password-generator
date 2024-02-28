# Create a program that generates a random
# password of a user-defined length

import random

def generate_password(length=int):
    # Define character sets
    rlist=''
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special_characters = "@#$%^&*."

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    for _ in range(length):
        x=random.choice(all_characters)
        rlist=rlist+x
    print(rlist)

generate_password(int(input('enter length of password: ')))

