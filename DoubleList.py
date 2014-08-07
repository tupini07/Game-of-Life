class DoubleList(list):
    def __getitem__(self, key):
        return super(DoubleList, self).__getitem__(key-1)
    '''
    For the purpose of making a 'board' that has no edges there is the need for a double list
    
    in a double list the item befor the first is the last and the one after
    the last is the first
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(DoubleList, self).__init__()
    
    def __str__(self):
        ster = ""
        for e in self.__iter__():
            ster += str(e)
        return ster
        