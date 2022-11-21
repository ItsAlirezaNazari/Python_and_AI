num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))

if num1 > num2:
    greater = num2
else:
    greater = num1

for i in range(greater, num1 * num2 + 1):
    if((i % num1 == 0) and (i % num2 == 0)):
        lcm = i
        break

print("lcm for", num1, "and", num2, "is =", lcm)
