import string
import random
RESTRICTED = ["main.py", "secret_key.key", "crypt.py", "protected.py", "requirements.txt", "test.py"]
def name() -> str:
    NAME = string.octdigits
    NAME += string.ascii_uppercase
    NAME += string.digits
    NAME += str(random.randint(1, 100_000))
    NAME = ''.join(random.sample(NAME, len(NAME)))
    NAME += ".crypt"
    return NAME