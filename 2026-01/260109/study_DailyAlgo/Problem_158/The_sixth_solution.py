def solution(n):
    answer = True
    str_n = str(n)

    if str_n != str_n[::-1]:
        answer = False

    return answer

print(solution(131))
print(solution(12345))
print(solution(7))