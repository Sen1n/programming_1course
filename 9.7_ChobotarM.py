# alphabet = "abcdefghijklmnopqrstuvwxyz"
# length = int(input())
# ------------------------------------------------------------------------------------------#
# - створити ліст, в який додається елемент, якого не було повторено 2 рази?
# n = int(input())
# letters = []
# letters_on_cubes = input()
# for letter in letters_on_cubes:
#     letters.append(letter)
# for el in letters:
#     count = letters.count(el)
#     if count == 1:
#         print(el)
#         break
# else:
#     print("Ok")
# ------------------------------------------------------------------------------------
def missing_cube(n, cubes):
    cube_count = {}
    for cube in cubes:
        if cube in cube_count:
            cube_count[cube] += 1
        else:
            cube_count[cube] = 1
    for cube in cube_count:
        if cube_count[cube] % 2 == 1:
            return cube
    return "Ok"


n = int(input())
cubes = input()
result = missing_cube(n, cubes)
print(result)
