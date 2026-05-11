class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B) < len(A):
            A, B = B, A

        a = len(A)
        b = len(B)
        total = a+b
        half = total // 2

        l = 0
        r = a - 1
        while True:
            i = l + (r-l) // 2
            j = half - i - 2
            print(f"i:{i}, j:{j}")

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i+1] if i+1 < a else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j+1] if j+1 < b else float('inf')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)

                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2


            if Aleft > Bright:
                r = i - 1

            elif Bleft > Aright:
                l = i + 1
