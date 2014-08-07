'''
Created on Aug 6, 2014

@author: andrea
'''
class ref(object):
    ''' Pointers can be created just with mutable types of data (for example an array),
    but for sake of comprehension this class exists.
    An example of its usage can be:
     
     a = ref([1, 2])
     b = a
     print a.get()  # => [1, 2]
     print b.get()  # => [1, 2]

     b.set(2)
     print a.get()  # => 2
     print b.get()  # => 2
     '''
    def __init__(self, obj):
        self.obj = obj
    def get(self):
        return self.obj
    def set(self, obj):
        self.obj = obj