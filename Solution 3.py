n=int(input())
k=str(bin(n).replace('0b',''))
k=k.split('0')
k.sort(key=len)
print(len(k[-1]))
