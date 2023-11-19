a = input()
b = input()
if_no = False
for el in b:
    if el not in a:
        print("No")
        if_no = True
        break
if not if_no:
    print("Ok")
