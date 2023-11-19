# new_dict = {}
# x = {}
# for key, possible_values in x.items():  # ми проходим по парах, нам пройтись по всіх можливих
#     # значеннях циклом і тепер для цього значення перекладом буде ключ
#     #
#     for value in possible_values:
#         if value not in new_dict:
#             new_dict[value] = []
#
#         new_dict[value].append(key)
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
num_of_words = int(input())
words_to_translate = []
for _ in range(num_of_words):
    word_with_tr_to_lat = [str(el) for el in input().split()]
    word_with_tr_to_lat = [word.replace(',', '') for word in word_with_tr_to_lat]
    print(*word_with_tr_to_lat)
    words_to_translate += word_with_tr_to_lat[2::]
    words_to_translate.sort()

for word in words_to_translate:

