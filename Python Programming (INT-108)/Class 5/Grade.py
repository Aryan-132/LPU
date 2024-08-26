name = input("Enter your name: ")

total_marks=float(input("Enter your total marks: "))

if total_marks >= 90 and total_marks < 100:
    
    print("Grade A")
elif total_marks >= 80 and total_marks <= 90:
    print("Grade B")
    
elif total_marks >= 70 and total_marks <= 80:
    print("Grade C")
    
elif total_marks >= 60 and total_marks <= 70:
    print("Grade D")
    
else:
    print("Grade E")
    