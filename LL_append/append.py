class Node:
    def __init__(self, value):
        #pass
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node

        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):
        if self.length == 0:
           return 'list is empty'
        elif self.length == 1:
            temp = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return temp
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            return_val = temp.next.value
            temp.next = None
            self.length -=1
            self.tail = temp
            return return_val

    def prepend(self,value):
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def pop_first(self):
        if self.length ==0:
            return 'its an empty list'
        elif self.length == 1:
            return_val = self.head.value
            self.head = None
            self.tail = None
            self.length -=1
            return return_val
        else:
            return_val = self.head.value
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return return_val

    def Print_ll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next





my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.Print_ll()
print('fist pop 1', my_linked_list.pop_first())
my_linked_list.Print_ll()
print('fist pop 2', my_linked_list.pop_first())
my_linked_list.Print_ll()
print('fist pop 3', my_linked_list.pop_first())
my_linked_list.Print_ll()
print('fist pop 4', my_linked_list.pop_first())
my_linked_list.Print_ll()
print('fist pop empty', my_linked_list.pop_first())
my_linked_list.Print_ll()
# my_linked_list.prepend(0)
# print('after prepend')
# my_linked_list.Print_ll()
# print('number poped is ',my_linked_list.pop())
# print('number poped is ',my_linked_list.pop())
# print('number poped is ',my_linked_list.pop())
# print('number poped is ',my_linked_list.pop())
# print('number poped is ',my_linked_list.pop())


# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)



#dfsdfs