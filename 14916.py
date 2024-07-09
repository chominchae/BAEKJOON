import sys

money=int(input())
ans=0

while money>0:
	if money%5==0:
		ans+=money//5
		break
		
	money-=2
	ans+=1
	
if money<0:
	print(-1)
	sys,exit()
else:
	print(ans)
