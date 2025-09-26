import random
import sys

num = random.randint(1, 10)
print("skeftomai enan arithmo apo 1 mexri to 10")

guess = int(input("mantepse ton arithmo m:  "))

if guess == num:
    print(f"to vrikes, {num}")
else:
    print(f"exases, {num}")

print("done")
sys.exit()

