import sys
T = int(input())
ans=[]
for _ in range(T):
    N = int(input())  # 정수 개수 입력
    integer_list = list(map(int, input().split()))  # 정수 리스트 입력

    TorF=True 
    isIn = 0  # 검사한 정수의 개수
    start = 1 
    cycle_count = 0
    examined_set = set()
    
    end = integer_list[0]
    examined_set.add(1)

    while isIn < N:
        examined_set.add(end)
        
        if start == end:  # 사이클이 만들어지는 경우
            cycle_count += 1
            while TorF:
                if start+1 not in examined_set:
                    start += 1
                    break
                else:
                    start+=1      
            if start>N or start<0:
                break
            else:
                end=integer_list[start-1]    

        else:  # 사이클이 만들어지지 않는 경우 다음 값 조사
            end = integer_list[end - 1]

        isIn += 1
    ans.append(cycle_count)

for _ in ans:
    print(_)
