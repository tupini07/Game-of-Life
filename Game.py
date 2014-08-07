import copy
import os
import time

from Board import Board
from GameRules import GameRules


class Game(object):
    '''
    The main game logic
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.main_board = Board(GameRules.grid_size)
        self.gen_number = 0 #to keep track of which generation we are currently in
        self.born_cells = 0 #keep track of cells that are born
        self.died_cells = 0 #keep track of cells that die
        self.running = True #keep track of the simulation status
    
    def pause(self):
        self.running = False
        
    def start(self):
        while self.running:
            self.run_life()
            self.gen_number += 1
            time.sleep(GameRules.time_between_gen)
    
    def run_life(self):
        '''
        checks every cell in the board to see if it must be turned on or off
        '''
        model_board = copy.deepcopy(self.main_board) # we make a copy so as to not run into crazy problems :)
        
        for node in self.main_board.get_node_list():
            neighbors = node.count_live_neighbors(model_board) 
            if neighbors == GameRules.cells_for_reproduction:
                node.born()
                self.born_cells += 1
            elif neighbors > GameRules.cells_for_overpopulation:
                node.die()
                self.died_cells += 1
            elif neighbors <= GameRules.cells_for_underpopulation:
                node.die()
                self.died_cells += 1
                
                
    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
            
        
        