class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 1
        adj = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[0:i] + "*" + word[i + 1:]
                adj[pattern].append(word)
            
        q = deque([beginWord])
        visited = set()

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[0:j] + "*" + word[j+1:]
                    neis = adj[pattern]
                    for nei in neis:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        
        return 0
