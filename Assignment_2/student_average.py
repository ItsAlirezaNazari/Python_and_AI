counter = 0
sum = 0

while True:
    grade = input("Grade: ")

    if grade == "exit":
        break

    counter += 1
    sum += float(grade)

avg = sum / counter
print("Student average: ", avg)
