class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.linked_list_str=''

    def insert_on_top(self, data):
        node=Node(data)
        node.next=self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node


    def print_second(self, node):
        self.linked_list_str = ''
        while node:
            self.linked_list_str+=str(node.data)
            last = node
            node = node.next
        print(self.linked_list_str)


    def print(self):
        if self.head is None:
            print('Empty list')
            return
        itr=self.head
        self.linked_list_str = ''
        while itr:
            self.linked_list_str+=str(itr.data)+'->'
            itr=itr.next

        print(self.linked_list_str)



if __name__=='__main__':
    ll=DoubleLinkedList()
    ll.insert_on_top(1)
    ll.insert_on_top(2)
    ll.insert_on_top(3)
    ll.insert_on_top(4)
    #ll.insert_on_end(100)
    ll.print()
    ll.print_second(ll.head)



