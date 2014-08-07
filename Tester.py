'''
Created on Aug 6, 2014

@author: andrea
'''
from DoubleList import DoubleList
from Board import Board
if __name__ == '__main__':
    po = DoubleList()
    po.append(234)
    po.append(299999)
    print( po, po[0], po[1],po[2])
    
    wer = Board(20)
    #print(wer)
    erer= wer.get_board()[0][2]
    print(erer.get_x_pos(), erer.get_y_pos())