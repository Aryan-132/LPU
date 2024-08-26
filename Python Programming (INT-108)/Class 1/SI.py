#Way to create a function for calculating Simple Interest
def SI(p,t,r):

    return (p*t*r)/100;
#Test the function

p=float(input("Enter Principal Value: "))
t=float(input("Enter the Time Periods:"))
r=float(input("Enter the Interest rate: "))

if SI<=100:
    
    tax=0
elif SI<=1000 and SI > 100:
    tax=0.05*SI
else:
     tax=0.1*SI
print(tax)
    


print("The Simple Interest is :",SI(p,t,r))

    