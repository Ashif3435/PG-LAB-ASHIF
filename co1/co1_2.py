s=int(input("enter starting year"))
e=int(input("enter ending year"))
if(s<e):
    print("leap year are",end=" ")
    for i in range(s,e):
        if(i%4==0 or i%400==0 and i%100!=0):
            print(i,end=" ")