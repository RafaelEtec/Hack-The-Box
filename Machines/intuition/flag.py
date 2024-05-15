import hashlib
import itertools
import string

AUTH_KEY_PREFIX = "UHI75GHI"
KNOWN_MD5_HASH = "0feda17076d793c2ef2870d7427ad4ed"
CHARSET = string.ascii_letters + string.digits
KEY_LENGTH = 4

def check_auth_key(suffix):
    key = f"{AUTH_KEY_PREFIX}{suffix}"
    return hashlib.md5(key.encode()).hexdigest() == KNOWN_MD5_HASH

for guess in itertools.product(CHARSET, repeat=KEY_LENGTH):
    if check_auth_key(''.join(guess)):
        print(f"Found auth key: {AUTH_KEY_PREFIX}{''.join(guess)}")
        break
else:
    print("Auth key not found.")
