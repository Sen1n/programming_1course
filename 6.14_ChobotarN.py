S = input()

for el in S:
    S = S.replace(' ', '').lower()
if S == S[::-1]:
    print("YES")
else:
    print("NO")
