def solution(n):
    answer = 0 # 손뼉치는 횟수

    # str_n = str(n)

    for i in range(1, n+1):
        str_i = str(i)
        if ("3" in str_i) or ("6" in str_i) or ("9" in str_i):
            answer += 1

    return answer

print(solution(10))
print(solution(26))
print(solution(40))