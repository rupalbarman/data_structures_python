from linkedlist import llist
from binarytree import btree

r= llist.Root()
a=[1,2,3,4,5]
for i in a:
    r.insert_end(i)
r.list_all()
r.insert_front(200)
r.list_all()
r.insert_after(400, 2)
r.list_all()
r.delete(4)
r.list_all()

head= btree.Tree()
head.insert(10)
head.insert(20)
head.insert(30)
head.insert(5)
head.inorder(head.root)