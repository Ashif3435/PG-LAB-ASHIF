n=[]
s=int(input("enter the lim"))
print("enter values")
i=0
while(i<s):
    num=input("")
    n.append(int(num))
    i=i+1
print("\n list after assigning:\n")
i=0
while(i<len(n)):
    if(n[i]>100):
        print("over")
    else:
        print(n[i])
    i=i+1