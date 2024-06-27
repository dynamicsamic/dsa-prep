def find_center(edges: list[list[int]]) -> int:
    """
    Leetcode. 1791. Find Center of Star Graph
    https://leetcode.com/problems/find-center-of-star-graph/description

    -----------------------------Description-----------------------------------
    There is an undirected star graph consisting of n nodes labeled from 1 to n 
    A star graph is a graph where there is one center node and exactly n - 1 
    edges that connect the center node with every other node.

    You are given a 2D integer array edges where each edges[i] = [ui, vi] 
    indicates that there is an edge between the nodes ui and vi. 
    Return the center of the given star graph.

    -----------------------------Constraints-----------------------------------
    : 3 <= n <= 105
    : edges.length == n - 1
    : edges[i].length == 2
    : 1 <= ui, vi <= n
    : ui != vi
    : The given edges represent a valid star graph.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: edges = [[1,2],[2,3],[4,2]]
    Output: 2
    Explanation: As shown in the figure above, node 2 is connected to every 
    other node, so 2 is the center.

    Example 2:
    Input: edges = [[1,2],[5,1],[1,3],[1,4]]
    Output: 1

    ------------------------------Algorithm------------------------------------
    Store all vertices in a counter dict and count number of their appearence.
    Then find the vertice with most counts.
    """
    counter = {}

    for pair in edges:
        u, v = pair
        counter[u] = counter.get(u, 0) + 1
        counter[v] = counter.get(v, 0) + 1

    max_count = 0
    center = None

    for k, v in counter.items():
        if v > max_count:
            max_count = v
            center = k
    
    return center


assert find_center([[1,2],[5,1],[1,3],[1,4]]) == 1
assert find_center([[1,2], [2,4], [3,2]]) == 2