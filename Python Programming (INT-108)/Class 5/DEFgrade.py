def findGrade(marks):
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    else:
        print("E")

name=input("Name: ")
marks=float(input("Enter marks out of 100"))
findGrade(marks)