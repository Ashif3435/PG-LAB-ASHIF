str1=input("enter the string")
wordlist=str1.split()
count= []
for w in wordlist:
    count.append(wordlist.count(w))
print("count of the occurrence:" + str(list(zip(wordlist, count))))
