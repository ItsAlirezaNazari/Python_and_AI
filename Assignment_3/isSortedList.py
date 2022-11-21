list = []
sorted = True

len = int(input("Enter length of list: "))

for i in range(len):
    item = int(input("Enter item: "))
    list.append(item)

print(list)

for i in range(1, len):
    if list[i] < list[i-1]:
        sorted = False
        break

if sorted:
    print("The list sorted")
else:
    print("The list dont sorted")
