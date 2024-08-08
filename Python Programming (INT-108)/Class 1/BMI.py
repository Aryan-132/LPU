#BMI Caculator
def BMI(w,h):
    return w/(h**2)

w=float(input("Enter your weight in KGs: "))
h= float(input("Enter your height in Meters: "))

print("Your BMI is:", BMI(w,h))

if BMI(w,h)< 18:
    print("You are underweight")
elif BMI(w,h) >= 18 and BMI(w,h) <= 24.9:
    print("You are normal weight")
else:
    print("You are overweight")
    

