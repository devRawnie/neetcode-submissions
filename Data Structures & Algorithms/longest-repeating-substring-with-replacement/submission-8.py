class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frq_map = [0]*26
        i = 0
        j = 0
        res = 0
        max_freq = 0
        ORD_A = ord('A')
        while j < len(s):
            frq_map[ord(s[j])-ORD_A] += 1
            window_size = j-i+1
            if window_size - max(frq_map) <= k:
                res = max(res, window_size)
            else:
                frq_map[ord(s[i])-ORD_A] -= 1
                i += 1
            j += 1

        return res