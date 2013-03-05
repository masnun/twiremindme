import random, string

def generate_pin():
    return ''.join([random.choice(string.digits) for x in range(4) ])
