w = float(input())
h = float(input())

bmi = w / h ** 2

if bmi < 18.5:
    result = "Underweigth"
elif bmi >= 18.5 and bmi <= 24.9:
    result = "Normal weigth"
elif bmi >= 25 and bmi <= 29.9:
    result = "Overweigth"
elif bmi >= 30 and bmi <= 34.9:
    result = "Obesity"
elif bmi >= 35 and bmi <= 39.9:
    result = "Extreme Obesity"

print(result)
