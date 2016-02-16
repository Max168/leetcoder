class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for indx,val in enumerate(nums):
            hash_map[val] = indx

        for ind1,val in enumerate(nums):
            if target-val in hash_map:
                ind2 = hash_map[target-val]
                if ind1 != ind2:
                    return ind1+1,ind2+1

    def twoSum_update(self,nums,target):
        num = nums
        for ind1,val in enumerate(num):
            if target-val in num:
                return ind1+1,num.index(target-val)+1
