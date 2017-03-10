
class Node(object):
    def __init__(self, data):
        self.data=data
        self.next= None

class Root:
    def __init__(self):
        self.root= None

    def insert_end(self, data):
        if self.root== None:
            self.root= Node(data)
        else:
            x= self.root
            while x.next!= None:
                x= x.next
            x.next= Node(data)

    def insert_front(self, data):
        if self.root== None:
            self.root= Node(data)
        else:
            x= self.root
            self.root= Node(data)
            self.root.next=x

    def insert_after(self, data, index):
        if self.root==None:
            self.root= Node(data)
        else:
            x= self.root
            idx=0
            while x!=None:
                x= x.next
                idx+=1
                if idx== index:
                    y= x.next
                    x.next= Node(data)
                    x.next.next= y
                    break

    def delete(self, data):
        if self.root== None:
            print("Empty list")
        else:
            x= self.root
            while x.next:
                if x.next.data == data:
                    x.next= x.next.next
                    break
                x= x.next

    def list_all(self):
        x= self.root
        while x!= None:
            print(x.data, end= " ")
            x= x.next
        print()
