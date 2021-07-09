from video import Video, YouTube

class Linked_List:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def delete(self, current, before):
        #set before to current.next
        if current.next == None:
            before.next = None
            return None

        elif current == self.head:
            self.head = current.next
            return self.head

        before.next = current.next

        return before.next
        


    #def sort(self):
