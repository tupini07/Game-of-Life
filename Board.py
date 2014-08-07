from LifeNode import LifeNode
from DoubleList import DoubleList
class Board(object):
    '''
    This is the matrix representation of the board, and it has all the functions
    that make the matrix behave like an actual board
    '''


    def __init__(self, size):
        '''
        Constructor
        '''
        self.node_array = []  # so it doesn't have to scan all the matrix in order to access every node
                              # mainly for using with Injector
        self.matrix = DoubleList()
        for e in range(size):
            self.matrix.append(DoubleList())
            for i in range(size):
                node = LifeNode(i, e)
                self.matrix[e].append(node)
                self.node_array.append(node) # a list with pointers, each of them pointing to one node
    
    
    def get_node_list(self):
        return self.node_array
    
    def get_board(self):
        return self.matrix
    
    
    def __iter__(self):
        for row in self.matrix:
            yield row
    
    def __str__(self):
        ster = ""
        for row in self.matrix:
            ster += str(row) + "\n"
        return ster
        
