n = int(input("Enter a num: "))

for i in range(n):
    if (i % 2) == 0:
        print("*", end="")
    else:
        print("#", end="")

