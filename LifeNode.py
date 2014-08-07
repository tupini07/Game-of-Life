# -*- coding: UTF-8 -*-
# that strange UTF-8 stuff if there so that the interpreter lets me use the block simbols '▓' and '░'
class LifeNode(object):
    '''
    Each node represents a space in the grid (each cell), each one can be
    alive or dead, age and each one has knowledge of its position in the grid
    '''


    def __init__(self, x_pos, y_pos):
        '''
        Constructor
        '''
        self.alive = False
        self.age = 0  #-> still not implemented age
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def born(self):
        '''
        Sets the alive attribute to True
        The cell was born
        '''
        self.alive = True
        
    def die(self):
        '''
        Set the alive attribute to False
        The cell dies
        '''
        self.alive = False
    
    def is_alive(self):
        '''
        Tells if the cell is dead or alive
        '''
        return self.alive
    
    def toggle_life(self):
        '''
        Turns the cell alive if it's dead and turns it dead if it's alive
        This is mostly for using the 'Injector' 
        '''
        if self.alive:
            self.alive = False
        else:
            self.alive = True
            
    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos
    
    def get_age(self):
        return self.age
    
    def count_live_neighbors(self):
        pass
            
    def __str__(self):
        # if you have a better idea for this icons then you are welcomed to 
        # changed them
        if self.alive:
            return '▓'
        else:
            return '░'
        #return "(" +str(self.x_pos) + "," + str(self.y_pos) + ")"