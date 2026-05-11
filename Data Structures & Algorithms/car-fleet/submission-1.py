class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        n = len(speed)
        s_d = [(position[i],speed[i]) for i in range(n)]
        sorted_sd = sorted(s_d, key=lambda x: x[0])
        for i in range(n-1, -1, -1):
            time_taken = (target - sorted_sd[i][0]) / sorted_sd[i][1]
            if not stack:
                stack.append(time_taken)
            elif stack[-1] < time_taken:
                stack.append(time_taken)

        return len(stack)