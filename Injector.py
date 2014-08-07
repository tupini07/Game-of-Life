from GameRules import GameRules
class Injector(object):
    '''
    Toggles the 'alive' attribute of random cells in a board on and off
    '''


    def __init__(self, num_cells):
        '''
        Constructor
        Sets the number of cells that it toggles every time it runs
        '''
        self.num_cells = num_cells
    
    def inject(self, board):
        GameRules.grid_size