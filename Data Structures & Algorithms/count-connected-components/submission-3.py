class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find
        # n size list where each element holds its own index
        # for each edge in the list, find the parents of both nodes and make one the parent of the other
        # loop through the list and insert to a set and find the length of the set to get the number of connected components

        def find(node: int, result: list[int]) -> int:
            if result[node] == node:
                return node
            while result[node] != node:
                # path compression
                # result[node] = result[result[node]]
                node = result[result[node]]
            return node
            
        def union(node_a: int, node_b: int, result: list[int]) -> int:
            a, b = find(node_a, result), find(node_b, result)
            if a == b:
                return 0
            if rank[a] < rank[b]:
                result[a] = b
                rank[b] += rank[a]
            else:
                result[b] = a
                rank[a] += rank[b]
            return 1

        result = [x for x in range(n)]
        rank = [1] * n
        components = n
        for a, b in edges:
            components -= union(a, b, result)
        return components
