class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = {}
        in_degree = {}

        for w in words:
            for c in w:
                if c not in adj_list:
                    adj_list[c] = set()
                    in_degree[c] = 0

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            for z in range(minLength):
                if w1[z] != w2[z]:
                    if w2[z] not in adj_list[w1[z]]:
                        adj_list[w1[z]].add(w2[z])
                        in_degree[w2[z]] +=1
                    break

        queue = []

        for let in in_degree:
            if in_degree[let] == 0:
                queue.append(let)

        result = []

        while queue:
            current = queue.pop(0)

            result.append(current)
            for neighbor in adj_list[current]:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        output = ""
        for let in result:
            output+=let
        if len(output) != len(adj_list):
            return ""
        return output

        
