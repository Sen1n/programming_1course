n = int(input())
string_bin = ""
while n > 0:
    remainder = n % 2
    string_bin += str(remainder)
    n //= 2

string_bin = string_bin[::-1]
replaced_1_0 = string_bin.replace('1', 'SX').replace('0', 'S')
replaced_1_0 = replaced_1_0[2::]
print(replaced_1_0)
