x=float(input("Enter the investment:"))
y=int(input("Enter the number of years:"))
z=int(input("Enter the rate as %:"))
print("Year\t\tStarting balance\t\tInterest\t\tEnding balance")

for num in range(0,y):
    i=(x*z)/100
    n=i+x
    print(num,"\t\t",x,"\t\t\t",i,"\t\t\t",n)
    x=n
    
