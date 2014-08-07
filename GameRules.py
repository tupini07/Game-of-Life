class GameRules(object):
    '''
    specifies different rules for how the game works. If you want to change
    something then just change one of this parameters
    '''
    
    # define the exact number of neighbors the cell needs to be born
    cells_for_reproduction = 3
    
    # if the neighbors are more than this then the cell dies because of overpopulation
    cells_for_overpopulation = 3 # more than
    
    # number of neighbors that cause underpopulation
    cells_for_underpopulation = 2 # or less

    # if the injector function should be on or not
    injector = True
    
    # how many generations pass before injector acts
    injector_gens = 3
    
    # how many cells does injector alter each time it acts
    injector_actions = 4
    
    # time in s between each generation
    time_between_gen = 3
    
    # size of the grid, it's a square so it'll be x*x
    grid_size = 5
        