n=int(input("enter the number of terms :"))
n1=0
n2=1
count=0
if n<=0:
    print("Entered number is invalid")
elif n==1:
    print("Fibonnaci sequence of first",n,"terms is : ")
    print(n1)
else:
    print("fibonnaci sequence :")
    while count<n:
        print(n1)
        temp=n1+n2
        n1=n2
        n2=temp
        count += 1
