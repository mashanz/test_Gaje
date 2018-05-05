def solution(A):
    # write your code in Python 3.6
    tmp = 0
    n = 0
    tuker = 0
    for a in A:
    	if n < len(A)-1:
    		if a<=A[n+1]:
    			pass
    		else:
    			tmp = n
    		if(tmp>0):
    			if(A[tmp]>=A[n+1]) and n!=len(A)-2:
    				pass
    			else:
    				tuker += 1
    				x = A[tmp]
    				A[tmp] = A[n]
    				A[n] = x
    		n+=1
    n = 0
    tmp = 0
    for a in A:
    	if n < len(A)-1:
    		if a<=A[n+1]:
    			pass
    		else:
    			tmp = n
    		if(tmp>0):
    			if(A[tmp]>=A[n+1]) and n!=len(A)-2:
    				pass
    			else:
    				tuker += 1
    				x = A[tmp]
    				A[tmp] = A[n]
    				A[n] = x
    		n+=1
    if tuker>1:
    	return False
    else:
    	return True

A = [1,5,3,3,7]
B = [1,3,5,3,4]
C = [1,2,4,6,3,7,9,8]
D = [1,5,2,8,2,0,0,9,8,2,5,3]
E = [1,3,5]
print(solution(B))
