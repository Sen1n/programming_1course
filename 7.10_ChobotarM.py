# def conversion_to_decimal(number_to_conv, system_of_):
#     while number_to_conv > 0:
#         lst_with_num = []
#         remainder = number_to_conv % system_of_
#         number_to_conv //= system_of_
#         lst_with_num.append(remainder)       -   -  -- - - - - - - - перша ідея
#         return True ---?????????????
def decimal_to_other_sys(number, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result  # конкатенація рулить
        number //= base
    return result


m, k = [int(el) for el in input().split()]
number = int(input())
result = decimal_to_other_sys(number, k)
print(result)
