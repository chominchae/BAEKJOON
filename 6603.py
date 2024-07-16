def backtracking(numbers, start, selected):
    if len(selected) == 6:  # 6개의 숫자를 선택한 경우
        print(" ".join(map(str, selected)))
        return
    
    for i in range(start, len(numbers)):
        selected.append(numbers[i])
        backtracking(numbers, i + 1, selected)
        selected.pop()  # return 이후 끝난 후에 선택된 숫자를 제거해야 함

import sys

input_lines = []
while True:
    line = input().strip()
    if line == "0":
        break
    input_lines.append(line)

for line in input_lines:
    numbers = list(map(int, line.split()))
    k = numbers[0]
    numbers = numbers[1:]

    backtracking(numbers, 0, [])
    print()  # 각 케이스 출력 사이에 빈 줄 추가
