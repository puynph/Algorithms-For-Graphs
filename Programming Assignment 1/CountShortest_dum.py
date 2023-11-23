from graafi import Graph


"""Function that follows similar logic to BFS algorithm to calculate the
maximum amount of subset vertices in shortest path.
Returns either the subset vertex count as a positive integer or a 0 if 
there is no path to vertex t.
"""
def CountShortest(g, S, s, t):
    # This will be the length to t when it is found and is used to break loop.
    shortest_path = False
    # Same as in BFS, vertices are stored in que
    que = [s]
    # Paths can have different amount of subset vertices so they are stored
    # in a list for comparison
    list_of_paths = []
    # Each vertex in the graph has a distance, but the starting vertex
    # has a distance of 0
    d = {s: 0}
    # Vertices that belong to chosen subset are tracked
    # similar way as distance.
    subset_count = {}
    # Following for loop initializes distances and subset count for each
    # vertex in graph g.
    for vertex in g.V:
        d[vertex] = False
        if vertex in S:
            subset_count[vertex] = 1
        else:
            subset_count[vertex] = 0
    # If t is never found, que will eventually empty itself and end the loop.
    while que:
        vertex = que[0]
        current_distance = d[vertex]
        # If the final vertex is found, loop execution stops even if que
        # has elements in it.
        if current_distance > shortest_path != False:
            break
        que.pop(0)
        # All vertices that are reachable from the current vertex are checked.
        for adjacent in g.AL[vertex]:
            if d[adjacent] < current_distance + 1 and adjacent != t:
                d[adjacent] = current_distance + 1
                if not shortest_path:
                    que.append(adjacent)
            if adjacent in S:
                subset_count[adjacent] = subset_count[vertex] + 1
            else:
                subset_count[adjacent] = subset_count[vertex]
            if adjacent == t:
                list_of_paths.append(subset_count[adjacent])
                shortest_path = current_distance
    # Function sorts the list of different paths to t in descending order
    # and picks the first element, since it has the highest subset vertex
    # count.
    if list_of_paths:
        return sorted(list_of_paths, reverse=True)[0]
    # If list_of_paths is empty, it means that t was never reached and there
    # exist no path, in this case function returns 0.
    else:
        return 0

