class GameRules(object):
    '''
    specifies different rules for how the game works. If you want to change
    something then just change one of this parameters
    '''
    
    # define the number of neighbors the cell needs to be born
    cells_for_reproduction = 3
    
    # maximum number of neighbors before the cell dies because of overpopulation
    cells_for_overpopulation = 3 #or more
    
    # number of neighbors that cause underpopulation
    cells_for_underpopulation = 2 # or less

    # if the injector function should be on or not
    injector = True
    
    # how many generations pass before injector acts
    injector_gens = 20
    
    # how many cells does injector alter each time it acts
    injector_actions = 4
    
    # time in ms between each generation
    time_between_gen = 1000
    
    # size of the grid, it's a square so it'll be x*x
    grid_size = 5
        