
class node:
    def __init__(self, data_val=None):
        self.data_val = data_val
        self.next_node = None


class Linked_list:
    def __init__(self):
        self.head = None

    def add_new_node(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next_node:
                last_node = last_node.next_node
            last_node.next_node = new_node

    def list_out(self):
        value_to_print = self.head
        while value_to_print is not None:
            print(value_to_print.data_val)
            value_to_print = value_to_print.next_node


def main():
    list_ = Linked_list()
    print("Empty node in list: ", list_)
    list_.head = node(5)
    a1 = node(6)
    a2 = node(7)
    list_.head.next_node = a1
    a1.next_node = a2
    list_.add_new_node(22)
    list_.list_out()
    print(list_)


if __name__ == '__main__':
    main()


