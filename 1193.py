num=int(input())
line=1

while num > line:
        num -= line
        line += 1
i=1
if line%2==1:
        a=line-num+1
        b=num
elif line%2==0: 
        a=num
        b=line-num+1
        
print(f'{a}/{b}')
