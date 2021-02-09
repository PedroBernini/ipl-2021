# Programa para encontrar valores máximos em uma estrutura chamada "árvore".

def binary_tree_max(tree):
    if tree['children'] == []:
        return tree['value']
    return max([binary_tree_max(tree['children'][0]), binary_tree_max(tree['children'][1]), tree['value']])

def tree_max(tree):
    return max([tree_max(children) for children in tree['children']] + [tree['value']])