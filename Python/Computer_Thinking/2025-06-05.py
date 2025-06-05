def merge_sort(a) :
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료수가 한개 이하라면 GG
    if n <= 1 :
        return a
    
    mid = n // 2 # 중간을 두 그룹으로 쪼개기
    g1 = merge_sort(a[:mid]) # 재귀호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀호출로 두 번째 그룹을 정함
                #  ^^~~~~~~~
                # 이 부분은 python에만 있는 특수한 파싱문법임
    # 두 그룹을 하나로 병합
    result = [] # 두 그룹을 합친 결과
    while g1 and g2 : #두 그룹에 자료가 남아있으면 반복
        if g1[0] < g2[0] : #두 그룹 맨 앞 자료 비교
            # g1의 값이 더 작으면 그걸 추출해서 결과로 저장
            result.append(g1.pop(0))
        else :
            # g2 값이 더 작으면 g2으로 저장
            result.append(g2.pop(0))
    # 남아있는 자료들을 계속 찾아 저장
    # g1과 g2중 빈 것은 while문을 지나감
    while g1 :
        result.append(g1.pop(0))
    while g2 :
        result.append(g2.pop(0))
    return result

d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))