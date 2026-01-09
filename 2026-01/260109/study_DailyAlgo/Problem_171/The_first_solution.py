def solution(numbers):
    # 1. 빈 빈도수 딕셔너리 만들기
    counts = {}
    
    # 2. 직접 숫자를 돌며 개수 세기
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    # 3. 가장 높은 빈도수 찾기
    max_freq = max(counts.values())
    
    # 4. 최대 빈도를 가진 숫자들 중 가장 작은 값 찾기
    max_candidates = []
    for num, freq in counts.items():
        if freq == max_freq:
            max_candidates.append(num)
            
    return min(max_candidates)

print(solution([1,2,2,3,3,3,4]))
print(solution([5,5,-2,-2,7]))
print(solution([10,-10,15,10,-10,15,9]))