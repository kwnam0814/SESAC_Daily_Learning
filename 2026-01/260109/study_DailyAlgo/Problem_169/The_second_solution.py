def solution(n):
    answer = 0 # 손뼉치는 횟수

    # str_n = str(n)

    for i in range(1, n+1):
        str_i = str(i)

        # if ("3" in str_i) or ("6" in str_i) or ("9" in str_i):
        #     answer = answer + (str_i.count("3")) + (str_i.count("6")) + (str_i.count("9"))

        for char in str_i:
            # char이 3, 6, 9니?
            if char in {'3', '6', '9'}:
                answer += 1

    return answer

print(solution(10))
print(solution(26))
print(solution(40))