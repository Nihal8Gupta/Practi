#WAP to print third max or maximum
class Solution:
    def thirdMax(self, nums) -> int:
        l=list(set(nums))
        l.sort()
        n=len(l)
        if n==3:
            return l[0]
        elif n>3:
            return l[n-3]
        else:
            return max(l)
obj=Solution()
print(obj.thirdMax([1,2,3,2,5]))