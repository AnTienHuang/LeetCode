# 269. Alien Dictionary
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        nodes = { c: set() for word in words for c in word }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    nodes[w1[j]].add(w2[j])
                    break
        res = []
        visit = {} # tracking status of characters: False = Visited, True = Visiting

        def dfs(parent):
            if parent in visit:
                return visit[parent]
            visit[parent] = True
            for child in nodes[parent]:
                if dfs(child):
                    return True
            visit[parent] = False # No longer in path but no need to add to res
            res.append(parent)

        for n in nodes:
            if dfs(n):
                return ""
        
        res.reverse()
        return "".join(res)