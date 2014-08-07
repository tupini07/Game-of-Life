class DoubleList(list):
    '''
    For the purpose of making a 'board' that has no edges there is the need for a double list
    
    in a double list the item before the first is the last and the one after
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
        
    def __getitem__(self, key):
        '''
        This class is not exactly a double list, however it gets the job done.
        when an item with an index that is out of bounds is asked then we suppose
        it's because the user wants the first item of the list
        '''
        if key < super(DoubleList, self).__len__():
            return super(DoubleList, self).__getitem__(key)
        else:
            return super(DoubleList, self).__getitem__(0)