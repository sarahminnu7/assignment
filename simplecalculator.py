print("CALCULATOR \n1.add \n2.substract \n 3.multiply \n 4.division ")
n=int(input("enter the choices:"))
if(n==1):
    n1=int(input("enter the number:"))
    n2=int(input("enter the number:"))
    n3=n1+n2
    print(n3)
elif(n==2):
    n1=int(input("enter the number:"))
    n2=int(input("enter the number:"))
    n3=n1-n2
    print(n3)
elif(n==3):
    n1=int(input("enter the number:"))
    n2=int(input("enter the number:"))
    n3=n1*n2
    print(n3)
elif(n==4):
    n1=int(input("enter the number:"))
    n2=int(input("enter the number:"))
    n3=n1/n2
    print(n3)
else:
    print("invalid choice")

