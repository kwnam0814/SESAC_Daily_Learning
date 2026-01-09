def solution(n):
    n = str(n)
    
    for left in range(len(n)):
        # print(left) : 0, 1, 2, 3, 4, ...
        # right 변수가 필요 : -1, -2, -3, -4, ...

        right = - 1 - left # 음의 인덱스 이용

        if n[right] != n[left]:
            return False
        
    return True

print(solution(131))
print(solution(12345))
print(solution(7))