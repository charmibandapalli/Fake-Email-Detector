import re
def is_fake(email):
    return not bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

print(is_fake("test@fakecom"))
