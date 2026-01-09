def solution(numbers):
    n = len(numbers)

    for i in range(n):
        number = numbers[i]

        if number != i+1:
            return i+1
        
    return n+1

print(solution([1,2,3,4,6,7]))
print(solution([2,3,4]))
print(solution([1,2,3]))