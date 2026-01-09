def solution(numbers):
    # 1. n의 값 결정 (리스트 길이에 빠진 숫자 1개를 더함)
    n = len(numbers) + 1
    
    # 2. 1부터 n까지의 이론적인 총합 계산
    expected_sum = (n * (n + 1)) // 2
    
    # 3. 현재 리스트에 들어있는 숫자들의 실제 합 계산
    actual_sum = sum(numbers)
    
    # 4. 두 값의 차이가 바로 빠진 숫자
    return expected_sum - actual_sum

print(solution([1,2,3,4,6,7]))
print(solution([2,3,4]))
print(solution([1,2,3]))