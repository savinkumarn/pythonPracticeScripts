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
        self.print_node()

    def add_node_at_beginning(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        self.print_node()

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

    def add_node_at_pos(self, data, pos):
        print(f"Adding element {data} at pos {pos}")
        if pos == 1:
            self.add_node_at_beginning(data)
            return
        curr = self.head
        for i in range(pos-2):
            curr = curr.get_next_node()
        new_node = Node(data)
        new_node.set_next_node(curr.get_next_node())
        curr.set_next_node(new_node)
        self.size += 1
        self.print_node()

    def print_node(self):
        curr = self.head
        list_to_print = []
        while curr:
            list_to_print.append(curr.data)
            curr = curr.get_next_node()
        print(list_to_print)

    def print_reverse_list(self, head):
        if head is None:
            return
        self.print_reverse_list(head.get_next_node())
        print(head.data)

    def print_list_recur(self, head):
        if head is None:
            return
        print(head.data)
        self.print_list_recur(head.get_next_node())

    def reverse_link_list(self, head):
        if head.get_next_node() is None:
            self.head = head
            return
        self.reverse_link_list(head.get_next_node())
        new_node = head.get_next_node()
        new_node.next_node = head
        head.next_node = None


def main_linked_list():
    my_list = LinkedList()
    print("Adding data at the beginning of node")
    my_list.add_node(5)
    my_list.add_node(15)
    my_list.add_node(45)
    my_list.print_node()
    print("Adding data at the end of node")
    my_list.add_node(99, True)
    my_list.add_node(12, True)
    my_list.add_node_at_pos(54, 3)
    my_list.add_node_at_pos(35, 5)
    my_list.add_node_at_pos(25, 1)
    my_list.print_list_recur(my_list.head)
    my_list.print_reverse_list(my_list.head)
    my_list.reverse_link_list(my_list.head)
    my_list.print_node()
    print("Size")
    print(my_list.get_size())
