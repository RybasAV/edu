a = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
s = list(dict.keys(a))
print(s) 
a1 = {} 
for i in range(len(s)):
	a1[a[s[i]]] = s[i]
s1 = list(dict.keys(a1))
print(s1)
