# Working but inefficient solution

class Solution:
    def reachableNodes(self, n, edges, restricted):
        def getAdjacencyList(n, edges, restricted):
            # Creates adjacency list eliminating edges adjacent to restricted nodes
            # Results in a forest with multiple connected components
            adjacency_list = [set()]*n
            for edge in edges:
                if edge[0] not in restricted and edge[1] not in restricted:
                    adjacency_list[edge[0]] = adjacency_list[edge[0]].union([edge[1]])
                    adjacency_list[edge[1]] = adjacency_list[edge[1]].union([edge[0]])
            return adjacency_list

        def getUnvisitedNeighbors(nodes, adjacency_list, visited):
            neighbors = set()
            for node in nodes:
                neighbors = neighbors.union(adjacency_list[node])
            neighbors = neighbors-visited
            return neighbors

        adjacency_list = getAdjacencyList(n, edges, restricted)

        visited = {0}
        nodes = [0]
        reachable = 1
        keep_going = True
        while keep_going:
            print(f"current nodes: {nodes}")
            nodes = getUnvisitedNeighbors(nodes, adjacency_list, visited)
            visited = visited.union(nodes)
            print(f"children: {nodes}")
            l = len(nodes)
            if l > 0:
                reachable += l
            else:
                keep_going = False
            print(f"# reachable nodes found so far: {reachable}")
            print("--------")
        return reachable

S = Solution()
S.reachableNodes(13,[[0,1],[1,2],[3,1],[4,0],[0,5],[5,6],[3,7],[7,8],[7,9],[2,10],[10,11],[10,12]],[4,5,10])

