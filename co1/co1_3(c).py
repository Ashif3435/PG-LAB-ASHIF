w=input("enter word:")
print("original word:",w)
print("vovles:",end=" ")
for i in w:
    if i in('A','E','I','O','U','a','e','i','o','u'):
        print(i,end=" ")