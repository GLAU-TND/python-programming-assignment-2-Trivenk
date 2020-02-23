l=list(map(str,input().split()))
k=[l[0]]
for i in k:
    for j in l:
       if i[-1]== j[0]:
           if j not in k:
               k.append(j)
               break  
print(k)
    
