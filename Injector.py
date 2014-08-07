from random import randint

from GameRules import GameRules


class Injector(object):
    '''
    Toggles the 'alive' attribute of random cells in a board on and off
    '''


    def __init__(self):
        '''
        Constructor
        Sets the number of cells that it toggles every time it runs
        '''
    
    def inject(self, board):
        '''
        toggles a random cell
        It repeats the process the number of times specified in the 'GameRules'
        I needs a board as a parameter, to know in which board does it have to insert
        '''
        for injector_action_num in range(GameRules.injector_actions): 
            rndCellIndex = randint(0, GameRules.grid_size ** 2 - 1)  # gets a random number between 0 and  the total of nodes in the board - 1 
            rndCell = board.get_node_list()[rndCellIndex] # gets the random cell
            rndCell.toggle_life() # if it's on turn it off, or viceversa
            
