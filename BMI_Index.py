def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
print("Welcome to the BMI Calculator")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
if weight <= 0 or height <= 0:
    print("Invalid inputs.. Weight and height must be positive numbers.")
else:
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
