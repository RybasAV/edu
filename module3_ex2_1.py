s = [1, 4, 1, 6, 'hello', 'a', 5, 'hello']
s2 = []
for i in range(len(s)):
	if s[i] not in s2:
		s2.append(s[i])
print(s)
print(s2)