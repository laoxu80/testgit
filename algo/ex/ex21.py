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

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        #rlist=[]
        res=[None]*n
        k=1
        for i in range(n):
            """
            rsum = 1
            lsum = 1
            for j in range(0,i):
                lsum = lsum * nums[j]
            for y in range(i+1,len_num):
                rsum = rsum * nums[y]
            newele =lsum*rsum
            rlist.append(newele)
            """
            res[i] = k  # 初始化化最左边元素的左边元素为1
            k = k * nums[i]  # 利用k存储左边元素的乘积
        k = 1  # 初始化k=1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * k  # 初始化最右边元素为其左边元素的乘积乘1
            k = k * nums[i]
        return res




if __name__=="__main__":
    nums_a = [29, 79, 119, 1598877]
    target_a = -2147483648
    re=Solution()
    #print(re.twoSum(nums=nums_a,target=target_a))
    print(re.productExceptSelf(nums_a))
