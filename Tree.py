import random


class Tree:
    def __init__(self, size=5):
        self.tree = dict()
        self.dept = dict()
        self.pnSize = size  # Total number of parent nodes

        self.build_tree()

    def build_tree(self):
        num = 1
        for i in range(1, self.pnSize):
            val_list = []
            for j in range(random.randint(1, 3)):
                num += 1
                self.max_node = num
                val_list.append(str(num))

            self.tree[str(i)] = val_list  # adding child nodes
        for i in range(self.pnSize, num+1):
            self.tree[str(i)] = []

    def initial_node(self):  # return first node from where the search starts
        return list(self.tree.keys())[0]

    def generate_goal(self, min_limit=1, max_limit=None):  # generate a random goal from the tree values
        self.max_node = int(list(self.tree)[-1])   # getting max number

        if (max_limit is None) or (max_limit > self.max_node) or (max_limit < 1):  # setting max_limit
            if max_limit is not None:
                print(f"Unable to set maximum limit...\nDefault minimum limit is {self.max_node}")
            max_limit = self.max_node
        if min_limit < 1 or min_limit >= self.max_node:  # setting min_limit
            print("Unable to set minimum limit...\nDefault minimum limit is 1")
            min_limit = 1
        if min_limit > max_limit:  # setting limits
            print(f"Unable to set minimum limit...\nDefault limit is 1 to {self.max_node}")
            min_limit = 1
            max_limit = self.max_node

        return random.randint(min_limit, max_limit)


# def route_finder(tree, node, route_list):
#     for parent, child in tree.items():
#         if node in child:
#             route_list.insert(0, parent)
#             break
#     if route_list[0] != list(tree.keys())[0]:
#         route_finder(tree, route_list[0], route_list)
#
#     return route_list
