class Stack:
    ''' Stack class implements a last in first out LIFO algorithm'''

    def __init__(self, from_list=None):
        if from_list is None:
            self.dataList = []
        else:
            self.dataList = from_list[:]  # make a copy

    def push(self, item):
        self.dataList.append(item)
        return self

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element

    def peek(self):
        return self.dataList[-1]

    def get_size(self):
        return len(self.dataList)

    def show(self):
        print('Stack is:', *reversed(self.dataList), sep='\n   ')
