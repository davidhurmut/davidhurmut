import random

a = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

b = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-",
    "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?", "/"]

    
c = ''.join(random.choice(a) for _ in range(4))
d = ''.join(str(random.randint(1, 10)) for _ in range(4))
e = ''.join(random.choice(b) for _ in range(4))
f = ''.join(random.choice(a) for _ in range(4))
g = ''.join(str(random.randint(1, 10)) for _ in range(4))
h = ''.join(random.choice(b) for _ in range(4))


password = c + d + e + f + g + h

print("Generated password:", password)

