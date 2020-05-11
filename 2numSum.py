#encoding:utf-8

# 暴力
class Solution:
    def twoSum(self, nums, target):
        arr_index = []
        for index, i in enumerate(nums):
            for j in range(index + 1, len(nums)):
                if i + nums[j] == target:
                    arr_index.append(index)
                    arr_index.append(j)
                    return arr_index
        return None

    def twoSum2(self, nums, target):
        arr_index = []
        value_index_dict = {}
        for i_index, value in enumerate(nums):
            value_index_dict[value] = i_index
        for i_index, value in enumerate(nums):
            value2 = target - value
            if value_index_dict[value2] and i_index != value_index_dict[value2]:
                arr_index.append(i_index)
                arr_index.append(value_index_dict[value2])
                return arr_index
        return None

    def twoSum3(self, nums, target):
        pass

