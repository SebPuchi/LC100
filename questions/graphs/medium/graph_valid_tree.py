class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ad_list = {}
        # create adjacenty list: 
        if len(edges) ==0:
            return True

        for i in range(len(edges)):
            node1 = edges[i][0]
            node2 = edges[i][1]
            neighbors1 = ad_list.get(node1, [])
            neighbors2 = ad_list.get(node2, [])
            neighbors1.append(node2)
            neighbors2.append(node1)
            ad_list[node1] = neighbors1
            ad_list[node2] = neighbors2

        connected_components = 0
        visited = []
        print(ad_list)
        for i in range(n):
            if i not in visited:
                stack = []
                stack.append(i)
                while len(stack) != 0:
                    current = stack.pop()
                    visited.append(current)
                    neighbors = ad_list[current]
                    for i in range(len(neighbors)):
                        if neighbors[i] not in visited:
                            stack.append(neighbors[i])
                        if neighbors[i] == current:
                            return False
                connected_components += 1
            
        return connected_components == 1 and len(visited) == n
