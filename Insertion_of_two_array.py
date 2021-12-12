class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []
        nums1.sort()
        nums2.sort()
        if len(nums2) != 1: 
            for i in nums1:
                for j in nums2:
                    if i == j : 
                        a.append(i)
                        nums1.remove(i)
                        break
            return a 
        elif len(nums2) == 1:
            for x in nums1 : 
                for y in nums2: 
                    if x == y : 
                        a.append(x)
                        nums1.remove(x)
                        break
            return a
