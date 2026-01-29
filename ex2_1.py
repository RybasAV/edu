spisok = [1, 4, 1, 6, "hello", "a", 5, "hello"]
print(spisok)
spisokpovt = []
for i in range(len(spisok)):
    if spisok.count(spisok[i]) > 1 and spisok[i] not in spisokpovt:
        spisokpovt.append(spisok[i])

print(spisokpovt)
