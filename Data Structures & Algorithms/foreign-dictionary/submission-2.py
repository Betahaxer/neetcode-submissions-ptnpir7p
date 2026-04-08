
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # words are non empty
        # return string with the valid order

        # why compare between adjacent pairs?

        # creates an adjacency list for all the characters that exist in the words array
        adj_list = {char:set() for word in words for char in word}

        # for each pair of words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            length = min(len(w1), len(w2))
            # invalid case if prefix is the same and w1 is longer than w2
            if len(w1) > len(w2) and w1[:length] == w2[:length]:
                return ""
            
            # only contain cases where w1 <= w2
            for x in range(length):
                # only add the first different character
                if w1[x] != w2[x]:
                    adj_list[w1[x]].add(w2[x])
                    break
        
        # as we are doing dfs in a graph
        # visited = {"a": False, "b": True}
        # False indicates visited, True indicates cycle (visited in current path)
        # if no entry means not visited yet
        visited = {}
        result = []
        # post order dfs
        def dfs(char: str) -> bool:
            # if visited alr, no point visiting again
            if char in visited:
                return visited[char]
            
            # else not visited, and visit current char
            visited[char] = True
            # process current char, visit all neighbours
            for neighbour in adj_list[char]:
                # if any of neighbours have cycles
                if dfs(neighbour):
                    return True
            result.append(char)
            # after processing node, mark as visited
            visited[char] = False
            return visited[char]

        for char in adj_list:
            if dfs(char):
                return ""
        # reverse string as post order dfs gives reverse order
        result = "".join(reversed(result))
        return result
