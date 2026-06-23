class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        main_map = {chr(n):0 for n in range(ord("a"), ord("z")+1)}
        nm = main_map.copy()
        for s in s1:
            main_map[s] = main_map.get(s, 0) + 1

        j = 0
        while j < len(s1):
            nm[s2[j]] += 1
            j += 1

        if main_map == nm:
            return True

        i = 0
        while j < len(s2):
            nm[s2[i]] = max(nm[s2[i]]-1, 0)
            nm[s2[j]] += 1
            i += 1
            j += 1
            if main_map == nm:
                return True

        return False

