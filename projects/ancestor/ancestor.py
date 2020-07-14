
def earliest_ancestor(ancestors, starting_node):
    # build graph
    verticies = {}
    for ancestor in ancestors:
        if ancestor[1] not in verticies:
            verticies[ancestor[1]] = set([ancestor[0]])
        else:
            verticies[ancestor[1]].add(ancestor[0])

    # DFT
    stack = []
    max_path = []

    stack.append([starting_node])

    while len(stack) > 0:
      current_path = stack.pop()
      current_node = current_path[-1]
      
      try:
        neighbors = verticies[current_node]
      except:
        if len(current_path) > len(max_path):
          max_path = current_path
        continue
      
      
      for neighbor in neighbors:
        stack.append(current_path + [neighbor])

    if max_path[-1] == starting_node:
      return -1
      
    return max_path[-1]