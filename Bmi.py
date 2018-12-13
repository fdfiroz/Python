name = (input())
feet = float(input())
inch = float(input())
weight_kg = float(input())
height_m = (feet*0.348)+(inch*0.0254)

bmi = weight_kg / (height_m**2)
print("bmi: ")  
print(bmi)
print(name)
if bmi<16:
    print("Severe Thinness")
elif bmi<=17:
    print("Moderate Thinness")
elif bmi<=18.5:
    print("Mild Thinness")
elif bmi<=25:
    print("Normal")
elif bmi <=30:
    print("Overweight")
elif bmi <=35:
    print("Obese Class I")
elif bmi <=40:
    print("Obese Class II")
elif bmi >=40:
    print("Obese Class III")