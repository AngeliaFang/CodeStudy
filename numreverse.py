"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
"""
import math

class Solution:

    def reverse(self, x):
        if x == 0:
            return x
        symbal = True
        if x < 0:
            symbal = False
        x = abs(x)
        x_str = str(x)
        x_str_re = x_str[::-1].lstrip("0")
        lowwer = str(2 ** 31)
        upper = str(2 ** 31 - 1)
        if len(x_str_re) == len(lowwer):
            for index in range(len(x_str_re)):
                if symbal:
                    if x_str_re[index] > upper[index]:
                        return 0
                    elif x_str_re[index] == upper[index]:
                        continue
                    else:
                        return int(x_str_re)
                else:
                    if x_str_re[index] > lowwer[index]:
                        return 0
                    elif x_str_re[index] == lowwer[index]:
                        continue
                    else:
                        return (0 - int(x_str_re))
        elif len(x_str) < len(upper):
            if symbal:
                return int(x_str_re)
            else:
                return (0 - int(x_str_re))

solution = Solution()
print(solution.reverse(-123))
