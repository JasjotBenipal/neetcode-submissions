class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numsa, numsb = nums1, nums2
        if len(nums2) < len(nums1):
            numsa = nums2
            numsb = nums1
        
        left1, left2 = 0, 0
        right1, right2 = len(numsa) - 1, len(numsb) - 1
        total = len(nums1) + len(nums2)
        half = total // 2

        while True:
            mida = (left1 + right1) // 2
            midb = half - mida - 2

            Aleft = numsa[mida] if mida >= 0 else float("-inf")
            Aright = numsa[mida + 1] if mida < len(numsa) - 1 else float("inf")
            Bleft = numsb[midb] if midb >= 0 else float("-inf")
            Bright = numsb[midb + 1] if midb < len(numsb) - 1 else float("inf")

            #correct partiion
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2 != 0:
                    return min(Aright, Bright)
                #even
                else:
                    return (max(Aleft, Bleft) + min(Bright, Aright)) / 2
            # incorrect partition
            elif Aleft > Bright:
                right1 = mida - 1
            elif Aright < Bleft:
                left1 = mida + 1





        left1, left2 = 0
        right1, right2 = nums