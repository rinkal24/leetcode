class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for node in range(len(graph)):
            if node not in color:
                s = [node]
                color[node] = 0
                while s:
                    val = s.pop()
                    for n in graph[val]:
                        if n not in color:
                            color[n] = color[val] ^ 1
                            s.append(n)
                        elif color[n] == color[val]:
                            return False
        return True
                