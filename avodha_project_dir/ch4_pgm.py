#BMI calculator
def bmi_calculator():
    weight=int(input("Enter your weight in kg:"))
    height=float(input("Enter your height in m2:"))
    bmi=weight/height
    bmi=round(bmi,2)
    return bmi
print("Body mass index is:",bmi_calculator())
