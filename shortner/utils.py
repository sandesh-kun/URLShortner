from .models import UniformResourceLocator
import random
import string

def generate_short_url():
    URL_LENGTH = 6
    is_unique = False

    while not is_unique:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=URL_LENGTH))
        is_unique = not UniformResourceLocator.objects.filter(shortened_url=short_url).exists()

    return short_url
