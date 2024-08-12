N=int(input())
integer_list=[0]*N
sum=0

integer_list = list(map(int, input().split()))  # 정수 리스트 입력

integer_list.sort()

for i in range(N):
    sum+=integer_list[i]*(N-i)

print(sum)
