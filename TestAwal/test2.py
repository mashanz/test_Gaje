def soulution(A,B):
    out = -1
    # write your code in Python 3.6
    A = sorted(A, key=int)
    B = sorted(B, key=int)
    for a in A:
        for b in B:
            if a == b:
                out = a
                break
        if out == a:
            break
    return out

A = [1,3,2,1]
B = [4,2,5,3,2]
print(soulution(A,B))