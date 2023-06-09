# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
def repeatedNTimes(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)/2
        for key,val in count.items():
            if val==n:
                return key