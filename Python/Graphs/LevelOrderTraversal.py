class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array=None):
        #for child in array:
        #    self.addChild(child)
        result = []
        queue = [self]
        while len(queue) > 0:
            visited = queue.pop(0)
            result.append(visited.name)
            while len(visited.children) > 0:
                toVisit = visited.children.pop(0)
                queue.append(toVisit)
        return result

'''
Input:
graph = A
      / | \
     B  C  D
    / \   /  \
   E   F G    H
      / \ \
     I   J K
Output:
 A B C D E F G H I J K 
'''
graph = Node("A")
graph.addChild("B")
graph.addChild("C")
graph.addChild("D")
graph.children[0].addChild("E")
graph.children[0].addChild("F")
graph.children[2].addChild("G")
graph.children[2].addChild("H")
graph.children[0].children[1].addChild("I")
graph.children[0].children[1].addChild("J")
graph.children[2].children[0].addChild("K")
print(graph.breadthFirstSearch())
