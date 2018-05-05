def solution(S):
	X = S.split(" ")
	s = ""
	for a in X:
		a = a[::-1]
		print(a)
		if s == "":
			s = s + a
		else:
			s = s + " " + a
	return(s)

S = "gabut coeg"
print(solution(S))