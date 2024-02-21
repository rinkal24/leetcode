class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                s = [node]
                color[node] = 0
                while s:
                    node = s.pop()
                    for n in graph[node]:
                        if n not in color:
                            s.append(n)
                            color[n] = color[node] ^ 1
                        elif color[n] == color[node]:
                            return False
        return True