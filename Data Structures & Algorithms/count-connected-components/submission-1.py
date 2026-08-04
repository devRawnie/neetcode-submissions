class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = [False for _ in range(n)]


        def dfs(i, cmp):
            if visited[i]:
                return

            visited[i] = True
            cmp.append(i)
            for e in adj_list.get(i, []):
                dfs(e, cmp)


        components = []
        for i in range(n):
            cmp = []
            dfs(i, cmp)
            if cmp:
                components.append(cmp)

        print(components)
        return len(components)
