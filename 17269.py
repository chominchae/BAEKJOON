dic = {'A': 3, 
       'B':2,
       'C':1,
       'D':2,
       'E':4,
       'F':3,
       'G':1,
       'H':3,
       'I':1,
       'J':1,
       'K':3,
       'L':1,
       'M':3,
       'N':2,
       'O':1,
       'P':2,
       'Q':2,
       'R':2,
       'S':1,
       'T':2,
       'U':1,
       'V':1,
       'W':1,
       'X':2,
       'Y':2,
       'Z':1}

N,M=map(int,input().split())
a,b=input().split()

new=[]
i=0

if N < M:
    while i < N:
        new.append(dic[a[i]])
        new.append(dic[b[i]])
        i += 1
    while i < M:
        new.append(dic[b[i]])
        i += 1
else:
    while i < M:
        new.append(dic[a[i]])
        new.append(dic[b[i]])
        i += 1
    while i < N:
        new.append(dic[a[i]])
        i += 1

length=len(new)

while length>2:
        temp=[]
        j=0
        while j<length-1:
                temp.append(((new[j]+new[j+1])%10))
                j+=1
        new=temp
        length=len(new)
  
if new[0]==0:
      print(f'{new[1]}%')
else:
     print(f'{new[0]}{new[1]}%')
