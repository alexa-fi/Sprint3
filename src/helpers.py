import random


def generate_email():
    email = str('5957099') + str(int(random.randint(100, 999))) + str('@gmail.com')
    return email
