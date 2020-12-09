A = "[(){()}]"

def check_parenthesis(A):
	s = []
	for i in range(len(A)):
		if A[i] in ["[", "{", "("]:
			s.append(A[i])
		else:
			if len(s) == 0:
				return False
			if s[-1] == "(" and A[i] == ")":
				s.pop()
			elif s[-1] == "[" and A[i] == "]":
				s.pop()
			elif s[-1] == "{" and A[i] == "}":
				s.pop()
			else:
				return False

	if len(s) == 0:
		return True
	else:
		return False

print(check_parenthesis(A))