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
        self.matrix = []
        for e in range(size):
            self.matrix.append(DoubleList())
            for i in range(size):
                self.matrix[e].append(LifeNode(i, e))
    
    
    def get_node_list(self):
        return self.node_array
    
    def get_board(self):
        return self.matrix
    
    def __str__(self):
        ster = ""
        for row in self.matrix:
            ster += str(row) + "\n"
        return ster
        
