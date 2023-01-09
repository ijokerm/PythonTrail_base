# 报纸拼接成匿名性
# import collections
# import math
    # def canConstruct(ransomNote,newspaper):
    #     from collections import Counter
    #
    #     dct_r = dict(Counter(ransomNote))
    #     dct_m = dict(Counter(newspaper))
    #     for i in ransomNote:
    #         if i not in dct_m or dct_r[i] > dct_m[i]:
    #             return  False
    #
    #     return True

class Solution:
    def canConstruct(self,ransomNote:str,newspaper:str) -> bool:
        newspaper_list = [x for x in newspaper]
        for i in ransomNote:
            if i in newspaper_list:
                newspaper_list.pop(newspaper_list.index(i))
            else :
                return False
        return True
rans = input()
news = input()
solution = Solution()
re = Solution.canConstruct(solution,rans,news)
print(re)