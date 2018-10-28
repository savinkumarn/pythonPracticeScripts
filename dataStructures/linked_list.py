class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, val):
        self.next_node = val


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node_at_end(self, data):
        curr = self.head
        while curr.get_next_node():
            curr = curr.get_next_node()
        new_node = Node(data)
        curr.set_next_node(new_node)
        self.size += 1

    def add_node_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def add_node(self, data, end=False):
        """
        :param data: node value
        :param end: if this parameter is set to True, the node is added at the end of list
        :return: nothing
        """
        if not end:
            self.add_node_at_beginning(data)
        else:
            self.add_node_at_end(data)

    def print_node(self):
        curr = self.head
        while curr:
            print(str(curr.data))
            curr = curr.get_next_node()


def main_linked_list():
    my_list = LinkedList()
    my_list.add_node(5)
    my_list.add_node(15)
    my_list.add_node(25)
    my_list.print_node()
    print("Adding at the end of node")
    my_list.add_node(99, True)
    my_list.add_node(12, True)
    my_list.print_node()
    print("Size")
    print(my_list.get_size())
