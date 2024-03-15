class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                Q = [node]

                while Q:
                    val = Q.pop()
                    for n in graph[val]:
                        if n not in color:
                            color[n] = color[val] ^ 1
                            Q.append(n)
                        elif color[n] == color[val]:
                            return False
        return True