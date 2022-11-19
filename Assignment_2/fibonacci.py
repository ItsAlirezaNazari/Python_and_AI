n = int(input("Enter number: "))

pre_previous = 0
previous = 1

print(previous, end=" ")

for i in range(n - 1):
    next = pre_previous + previous
    pre_previous = previous
    previous = next
    print(next, end=" ")
