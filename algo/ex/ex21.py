class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_num = {}
        for i,num in enumerate(nums):
            if target-num in dict_num:
                return [dict_num[target-num],i]
            else:
                dict_num[num]=i

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            xnew = int(str(x)[::-1])
        else:
            xnew = -int(str(-x)[::-1])
        if xnew >(2**31-1) or xnew < (-2**31):
            return 0
        else:
            return xnew



if __name__=="__main__":
    nums_a = [2, 7, 11, 15]
    target_a = -2147483648
    re=Solution()
    #print(re.twoSum(nums=nums_a,target=target_a))
    print(re.reverse(target_a))
