from itertools import permutations 
l=list(map(str,input().split()))
d=permutations(l)
k=[]
for i in d:
    s=''
    for j in i:
        s=s+j
    k.append(int(s))
print(max(k))

            
                
    
