class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        candidates.sort()
        def dfs(i, subs, n):
            if n == 0:
                result.append(subs.copy())
                return
            if i >= len(candidates):
                return
            if n < 0:
                return

            subs.append(candidates[i])
            dfs(i+1, subs, n-candidates[i])
            subs.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, subs, n)

        dfs(0, [], target)
        return result