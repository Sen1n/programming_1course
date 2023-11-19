# # 3 - к-сть тестів
# # 3 - чисел в них як я пон
# max_voice = []
#
# num_of_tests = int(input())
# while num_of_tests > 0:
#     voices = []
#     num_of_testing_nums = int(input())
#     num_of_tests -= 1
#     while num_of_testing_nums > 0:
#         test_num = int(input())
#         num_of_testing_nums -= 1
#         voices.append(test_num)
#     unique_numbers = set(voices)
#     if
#         print(min(unique_numbers))

num_of_tests = int(input())
while num_of_tests > 0:
    voices = []
    num_of_testing_nums = int(input())
    while num_of_testing_nums > 0:
        test_num = int(input())
        num_of_testing_nums -= 1
        voices.append(test_num)
    vote_count = {}
    for num in voices:
        if num in vote_count:
            vote_count[num] += 1
        else:
            vote_count[num] = 1
    max_votes = max(vote_count.values())
    popular_numbers = [num for num, votes in vote_count.items() if votes == max_votes]
    print(min(popular_numbers))
    num_of_tests -= 1
