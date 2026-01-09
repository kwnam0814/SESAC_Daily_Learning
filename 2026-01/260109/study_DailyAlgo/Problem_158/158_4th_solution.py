def solution(n):
    # answer = True
    str_n = str(n)

    for i in range(len(str_n)):
        if str_n[i] != str_n[len(str_n) - 1 - i]:
            return False
            break
        else:
            return True

    # return answer
    
print(solution(131))
print(solution(12345))
print(solution(7))