from collections import defaultdict
class Solution(object):
      

    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source >= n or destination >= n:
            return False
        if source == destination or [source, destination] in edges:
            return True
        graph = defaultdict(list)
        
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        seen = set()  
        
        def isValidPath(graph, source, destination):
            if source == destination:
                return True
            if source in seen:
                return False
            seen.add(source)
            return any(isValidPath(graph, src, destination) for src in graph[source])
        
        return isValidPath(graph, source, destination)