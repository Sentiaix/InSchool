# 2025 05 28 1st time

def find_min_idx(a) :
    n = len(a)
    min_idx = 0
    # (1, n, 1) 1부터 n - 1까지 1칸씩 증가
    for i in range(1, n) :
        if a[i] < a[min_idx] :
            min_idx = i
    return min_idx

def sel_sort(a) :
    result = []
    while a :
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))