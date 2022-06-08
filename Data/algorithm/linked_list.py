class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_on_top(self, data):
        node=Node(data,self.head)
        self.head=node
    def insert_on_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def print(self):
        if self.head is None:
            print('Empty list')
            return
        itr=self.head
        linked_list_str=''
        while itr:
            linked_list_str+=str(itr.data)+'-->'
            itr=itr.next

        print(linked_list_str)



if __name__=='__main__':
    ll=LinkedList()
    ll.insert_on_top(20)
    ll.insert_on_top(10)
    ll.insert_on_top(2)
    ll.insert_on_end(100)
    ll.print()



