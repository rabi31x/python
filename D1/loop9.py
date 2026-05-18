i = 7
a = 5
print("\n")
while i > 0:
    for j in range(5 - a):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    if i > 1:
        print("\n")
    i -= 2
    a -= 1