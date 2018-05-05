def solution(A, X):
    N = len(A)
    print("N = ",N)
    if N == 0:
        return -1
    l = 0
    r = N - 1
    while l < r:
        m = (l + r) // 2
        print("m = ",m)
        if A[l] == X:
            r = r - 1
            print("r = ",r)
        else:
            l = m
            print("l = ",l)
    if A[l] == X:
        return l
    return -1

A = [1,2,3,4]
X = 4
print(solution(A,X))