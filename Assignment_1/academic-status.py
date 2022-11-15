fname = input()
lname = input()
c1 = float(input())
c2 = float(input())
c3 = float(input())

avg = (c1 + c2 + c3) / 3
print("avg:", avg)

if avg >= 17:
    status = "Great"
elif avg < 17 and avg >= 12:
    status = "Normal"
elif avg < 12:
    status = "Fail"

print("status:", status)
