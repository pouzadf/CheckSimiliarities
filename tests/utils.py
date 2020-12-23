import random
import string


def create_random_word(length = 6, chars = string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(length))

def create_random_sentence(nb_words = 10):
    return " ".join(create_random_word() for _ in range(nb_words))    