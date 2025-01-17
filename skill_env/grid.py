##
## Maze class. Stores a configuration of tiles
##
from tile import Tile

class Grid:

    ##
    ##Grid contructor
    ##
    def __init__(self, grid_configuration):
        self.grid = self.grid_constructor(grid_configuration)

    ##
    ## Takes a list in the form ['quiet noise', 1, 1, 0 , 1] for example and constructs a tile.
    ##
    def tile_constructor(self, tile_configuration):
        audio_clip = tile_configuration[0]
        north_wall = True if (tile_configuration[1] == 0) else False
        south_wall = True if (tile_configuration[2] == 0) else False
        west_wall = True if (tile_configuration[3] == 0) else False
        east_wall = True if (tile_configuration[4] == 0) else False

        return Tile(north_wall, south_wall,  west_wall, east_wall, audio_clip)

    def row_constructor(self, row_configuration):
        grid_row = []
        for tile_configuration in row_configuration:
            grid_row.append(self.tile_constructor(tile_configuration))
        return grid_row

    def grid_constructor(self, grid_confirguation):
        grid = []
        for row_configuration in grid_confirguation:
            grid.append(self.row_constructor(row_configuration))
        return grid
    
    def print_row(self, row):
        for tile in row:
            tile.print_tile()
        print(' ')

    def print_grid(self):
        for row in self.grid:
            self.print_row(row)
    
    def get_tile(self, x_coordinate, y_coordinate):
        return self.grid[-y_coordinate][x_coordinate-1]

    
    def can_move(self, x_coordinate, y_coordinate, direction):
        current_tile = self.get_tile(x_coordinate, y_coordinate)
        if(direction == 'up'):  return not current_tile.north_wall
        elif(direction == 'down'): return not current_tile.south_wall 
        elif(direction == 'left'): return not current_tile.west_wall 
        elif(direction == 'right'): return not current_tile.east_wall
        else:
            return  
        
    
    

        
            
        





        
# Maze = [
# [['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0],['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,1], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',1,1,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]],
# [['',0,0,0,0],['',1,1,0,0], ['',1,1,0,0],['',1,1,0,0], ['',0,0,0,0], ['',0,0,0,0], ['',0,0,0,0]]] 

# #Test a Creating a Room
# G1 = Grid(grid_configuration = Maze)
# G1.print_grid()


# 
# Oringinal maze li 
#

