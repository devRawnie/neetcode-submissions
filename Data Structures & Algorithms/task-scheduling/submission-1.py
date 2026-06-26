class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        result = 0
        count = Counter(tasks)
        count_values = list(count.values())
        count_values.sort(reverse=True)
        maxf = count_values[0]
        idle = (maxf-1)*n
        for val in count_values[1:]:
            idle -= min(maxf-1, val)

        return len(tasks) + max(0, idle)