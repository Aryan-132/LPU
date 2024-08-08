#Way to create a function for calculating Simple Interest
def SI(p,t,r):

    return (p*t*r)/100;
#Test the function

p=float(input("Enter Principal Value: "))
t=float(input("Enter the Time Periods:"))
r=float(input("Enter the Interest rate: "))

print("The Simple Interest is :",SI(p,t,r))

    