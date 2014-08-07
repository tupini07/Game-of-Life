'''
Created on Aug 6, 2014

@author: andrea
'''
from DoubleList import DoubleList
from Board import Board
from GameRules import GameRules
if __name__ == '__main__':
    po = DoubleList()
    po.append(234)
    po.append(299999)
    print( po, po[0], po[1],po[2])
    
    wer = Board(5)
    print(wer)
    
    print(wer[2][2].is_alive())
    
    for e in wer.get_node_list():
        e.toggle_life()
    
    print (wer)
    
    print(wer[2][2].is_alive())
    print(wer[2][2].count_live_neighbors(wer))
    print (wer)
    
    print(wer[2][2].is_alive())
    print(wer[2][2].count_live_neighbors(wer))