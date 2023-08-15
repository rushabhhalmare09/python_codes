# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def findNode(head, n) :
    index = 0
    current = head
    while current is not None:
        if current.data == n:
            return index
        current = current.next
        index += 1
    return -1

Output: - Below 3 lines are Input values we need to provide after running the code
1
18 21 9 4 10 15 -1
4

3   ==> Answer
