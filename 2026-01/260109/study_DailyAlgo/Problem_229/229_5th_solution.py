def solution(numbers):
    n = len(numbers)

    numbers_set = set(numbers)
    full_set = set(range(1, n+2))

    remain_set = full_set - numbers_set
    
    return remain_set.pop()

print(solution([1,2,3,4,6,7]))
print(solution([2,3,4]))
print(solution([1,2,3]))