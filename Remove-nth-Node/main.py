class ListNode:
    def __init__(self, val, next=None):
         self.val = val
         self.next = next
    def yazdir(self):
        temp = head
        while temp !=None:
            print(temp.val)
            temp = temp.next
    def elemanEkle(self,eklenecekVeri):
        eklenecekDugum = ListNode(eklenecekVeri)
        eklenecekDugum.next = None
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = eklenecekDugum

    def elemanCikar(self,n):
        counter = 0
        temp = head
        if temp.next == None:
            return None
        while temp != None:
            temp = temp.next
            counter += 1
        temp = head
        if counter - n == 0:
            temp = head.next
            while temp != None:
                return temp
        for i in range(counter - n - 1):
            temp = temp.next
        temp.next = temp.next.next
        temp = head
        return temp





head = ListNode(1)
head.elemanEkle(2)
head.elemanEkle(3)
head.elemanEkle(4)
head.elemanEkle(5)
head.elemanCikar(0)
