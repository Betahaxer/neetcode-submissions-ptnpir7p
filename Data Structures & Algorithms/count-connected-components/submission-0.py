class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find
        # n size list where each element holds its own index
        # for each edge in the list, find the parents of both nodes and make one the parent of the other
        # loop through the list and insert to a set and find the length of the set to get the number of connected components


        def parent(node: int, result: list[int]) -> int:
            if result[node] == node:
                return node
            return parent(result[node], result) 

        def union(node_a: int, node_b: int, result:list[int]) -> None:
            result[parent(node_a, result)] = parent(node_b, result)

        # list where each element is its own index
        result = [x for x in range(n)]
        # store all parents
        distinct_components = set()

        for node_a, node_b in edges:
            union(node_a, node_b, result)
        
        for index, elem in enumerate(result):
            # add all parents to the set
            if elem == index:
                distinct_components.add(elem)

        return len(distinct_components)