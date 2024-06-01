# HOMEWORK: 객체 ABCDEFG 만들고, 샘플 123없애기
class Sample():

    nObjects = 0
    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('There are', Sample.nObjects, 'Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1

oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')
oSample5 = Sample('E')
oSample6 = Sample('F')
oSample7 = Sample('G')

del oSample1
del oSample2
del oSample3

print('Number of objects:', Sample.nObjects)