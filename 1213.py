# 문자열을 입력받아 알파벳 순서대로 정렬
str_input = sorted(input())
dic = {}
even = 0  # 짝수
odd = 0   # 홀수

# 각 문자의 빈도를 세는 과정
for char in str_input:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1

# 짝수와 홀수 개수를 세는 과정
for char, count in dic.items():
    if count % 2 == 0:
        even += 1
    else:
        odd += 1

# 홀수 개수가 1개 초과라면 팰린드롬 불가능
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    front_list = []
    center = ""  # 홀수 빈도의 문자는 가운데 위치

    for char, count in dic.items():
        # 짝수 빈도인 문자는 절반만큼 앞부분에 추가
        front_list.append(char * (count // 2))
        # 홀수 빈도의 문자는 가운데에 추가
        if count % 2 == 1:
            center = char

    # 앞부분을 결합하고, 뒤집은 뒤를 결합하여 팰린드롬 완성
    front = "".join(front_list)
    result = front + center + front[::-1]
    
    print(result)
