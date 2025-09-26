import sys

print("geia sou malaka")

try:
    a = float(input("vale ton prwto arithmo: "))
    b = float(input("vale ton deutero arithmo: "))
except ValueError:
    print("prepei na valeis arithmous")
    sys.exit()

print("\napotelesmata:")
print("prosthesi:", a + b)
print("afairesh:", a - b)
print("pollaplasiasmo:", a * b)

if b != 0:
    print("diairesh:", a / b)
else:
    print("diairesh: dn ginetai na diaireseis me to 0")

print("dynamh (a^b):", a ** b)

choice = input("\nthes na sunexiseis? (y/n): ").lower()
if choice == 'y':
    print("kanei restart to programma...")
else:
    print("eksodos apo to programma")
    sys.exit()

