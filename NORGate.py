# Nabiha Bashir
# This program stimulates a 2 input NOR Gate

#-------NOR Gate-------
print("NOR Gate")
# Get A & B values
norA = int(input("Enter a value for A (1 or 0): "))
norB = int(input("Enter a value for B (1 or 0): "))
# Display A & B
print("Your inputs A =", norA, "and B =", norB)
if (norA == 0) and (norB == 0):
    print("Make your statement TRUE \n")
else:
    print("Make your statement FALSE \n")
