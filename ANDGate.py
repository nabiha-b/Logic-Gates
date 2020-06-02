# Nabiha Bashir
#This program stimulates a 2 input AND Gate

#-------AND Gate-------
print("AND Gate")
# Get A & B values
andA = int(input("Enter a value for A (1 or 0): "))
andB = int(input("Enter a value for B (1 or 0): "))
# Display A & B
print("Your inputs A =", andA, "and B =", andB)
if (andA == 1) and (andB == 1):
    print("Make your statement TRUE \n")
else:
    print("Make your statement FALSE \n")
