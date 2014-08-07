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
    print( po, po[0], po[1])
    
    wer = Board(5)

    
    print (wer)
    print (wer.get_board()[-1][-1])