import random

input("Press Enter to roll dice")
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print("Rolled:", d1, "and", d2)
print("Total:", d1 + d2)
