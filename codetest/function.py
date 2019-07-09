class Function:
    def __init__(self):
        pass


    # 有效的数字只能由-，. 和数字构成，且负号只能有1个并且必须在第1位，小数点也只能有1个，数字至少必须有1个。
    # def check_number(self, number):
    #     is_valid = True
    #     is_correct = True
    #     point = 0
    #     minus = 0
    #     digit = 0
    #
    #     for char in number:
    #         ascii = ord(char)
    #         if ascii < 45 or ascii == 47 or ascii > 57:
    #             is_valid = False
    #             break
    #         if ascii == 46:
    #             point += 1
    #         if ascii == 45:
    #             minus += 1
    #         if ascii >= 48 and ascii <= 57:
    #             digit += 1
    #
    #     if is_valid and point <= 1 and minus <= 1 and digit >= 1:
    #         if minus == 1 and ord(number[0]) != 45:
    #             is_correct = False
    #         else:
    #             is_correct = True
    #     else:
    #         is_correct = False
    #
    #     return is_correct

    def check_number(self, number):
        is_valid = True
        is_correct = True
        point = 0
        minus = 0
        digit = 0

        for char in number:
            ascii = ord(char)
            if ascii < 45 or ascii == 47 or ascii > 57:
                is_valid = False
                break
            if ascii == 46:
                point += 1
            if ascii == 45:
                minus += 1
            if ascii >= 48 and ascii <= 57:
                digit += 1

        if is_valid and point <= 1 and minus <= 1 and digit >= 1:
            if minus == 1 and ord(number[0]) != 45:
                is_correct = False
            else:
                is_correct = True
        else:
            is_correct = False

        return is_correct