family_tree = {'root': ['child1', 'child2'],
               'child1': ['gc1', 'gc2'],
               'child2': ['gc3'],
               'gc3': ['ggc1', 'ggc2', 'ggc3']}


# depth first search
def dfs(node, tree, start, path):
    if start == node:
        return node
    if tree[start] == []:
        if start in path:
            path.remove(start)
        parent = path.pop()
        tree[parent].remove(start)
        return dfs(node, tree, parent, path)
    if start not in path:
        path.append(start)
    for child in tree[start]:
        if child in tree.keys():
            return dfs(node, tree, child, path)
        else:
            if child == node:
                return node
            tree[start].remove(child)
            return dfs(node, tree, start, path)
    return node + ' is not in this tree'


print(dfs('ggc1', family_tree, 'root', path=[]))
