'''
Created on Sep 8, 2017

@author: Joyce
'''
from moves import Moves


# call eval on these variables to carry out the string instructions
R_AWAY = 'Moves(self.cube_config).R_AWAY()'
R_TOWARDS = 'Moves(self.cube_config).R_TOWARDS()'
L_TOWARDS = 'Moves(self.cube_config).L_TOWARDS()'
L_AWAY = 'Moves(self.cube_config).L_AWAY()'
T_COUNTER_CLOCK = 'Moves(self.cube_config).T_COUNTER_CLOCK()'
T_CLOCK = 'Moves(self.cube_config).T_CLOCK()'
BM_RIGHT = 'Moves(self.cube_config).BM_RIGHT()'
BM_LEFT = 'Moves(self.cube_config).BM_LEFT()'
F_RIGHT = 'Moves(self.cube_config).F_RIGHT()'
F_LEFT = 'Moves(self.cube_config).F_LEFT()'
BA_LEFT = 'Moves(self.cube_config).BA_LEFT()'
BA_RIGHT = 'Moves(self.cube_config).BA_RIGHT()'
ROTATE_CLOCK = 'Moves(self.cube_config).ROTATE_CLOCK()'
ROTATE_COUNTER = 'Moves(self.cube_config).ROTATE_COUNTER()'
FLIP = 'Moves(self.cube_config).FLIP()'


# tuples indicating a row or column on the cube
right = (3,6,9)
left = (1,4,7)
top = (1,2,3)
bottom = (7,8,9)
cross = (2,4,6,8)



cube = {'front': {1: 'white', 2: 'white', 3: 'green', 4: 'red', 5: 'white', 6: 'orange', 7: 'blue', 8: 'orange', 9: 'orange'}, 
        'top': {1: 'red', 2: 'green', 3: 'white', 4: 'red', 5: 'blue', 6: 'red', 7: 'green', 8: 'green', 9: 'red'}, 
        'right': {1: 'yellow', 2: 'white', 3: 'orange', 4: 'yellow', 5: 'red', 6: 'green', 7: 'blue', 8: 'blue', 9: 'orange'}, 
        'left': {1: 'blue', 2: 'blue', 3: 'red', 4: 'yellow', 5: 'orange', 6: 'yellow', 7: 'yellow', 8: 'orange', 9: 'white'}, 
        'back': {1: 'green', 2: 'orange', 3: 'yellow', 4: 'red', 5: 'yellow', 6: 'green', 7: 'yellow', 8: 'yellow', 9: 'green'}, 
        'bottom': {1: 'red', 2: 'blue', 3: 'white', 4: 'white', 5: 'green', 6: 'white', 7: 'orange', 8: 'blue', 9: 'blue'}}



# maps the adjacent piece of every cross piece on each side
cross_adjacents = {'top': {2: ('back', 2), 4: ('left', 2), 6: ('right', 2), 8: ('front', 2)},
                   'front': {2: ('top', 8), 4: ('left', 6), 6: ('right', 4), 8: ('bottom', 2)},
                   'back': {2: ('top', 2), 4: ('right', 6), 6: ('left', 4), 8: ('bottom', 8)},
                   'bottom': {2: ('front', 8), 4: ('left', 8), 6: ('right', 8), 8: ('back', 8)},
                   'left': {2: ('top', 4), 4: ('back', 6), 6: ('front', 4), 8: ('bottom', 4)},
                   'right': {2: ('top', 6), 4: ('front', 6), 6: ('back', 4), 8: ('bottom', 6)}}



# maps bottom blue pieces to the correct algorithm that will translate them to the top
bottom_cross = {2: {'red': (BM_RIGHT, R_AWAY, R_AWAY), 'orange': (BM_LEFT, L_AWAY, L_AWAY), 
                    'white': (F_RIGHT, F_RIGHT), 'yellow': (BM_RIGHT, BM_RIGHT, F_RIGHT, F_RIGHT)},
                4: {'red': (BM_RIGHT, BM_RIGHT, R_AWAY, R_AWAY), 'orange': (L_AWAY, L_AWAY), 
                    'white': (BM_RIGHT, F_RIGHT, F_RIGHT), 'yellow': (BM_LEFT, BA_LEFT, BA_LEFT)},
                6: {'red': (R_AWAY, R_AWAY), 'orange': (BM_LEFT, BM_LEFT, L_AWAY, L_AWAY), 
                    'white': (BM_LEFT,F_RIGHT, F_RIGHT), 'yellow': (BM_RIGHT, BA_LEFT, BA_LEFT)},
                8: {'red': (BM_LEFT, R_AWAY, R_AWAY), 'orange': (BM_RIGHT, L_AWAY, L_AWAY), 
                    'white': (BM_RIGHT, BM_RIGHT, F_RIGHT, F_RIGHT), 'yellow': (BA_LEFT, BA_LEFT)}}



# either maps top pieces to the correct algorithm or to True, meaning the piece is already in the right place
top_cross = {2: {'red': T_CLOCK, 'orange': T_COUNTER_CLOCK, 'white': (T_CLOCK, T_CLOCK), 'yellow': True},
             4: {'red': (T_CLOCK, T_CLOCK), 'orange': True, 'white': T_COUNTER_CLOCK, 'yellow': T_CLOCK},
             6: {'red': True, 'orange': (T_CLOCK, T_CLOCK), 'white': T_CLOCK, 'yellow': T_COUNTER_CLOCK},
             8: {'red': T_COUNTER_CLOCK, 'orange': T_CLOCK, 'white': True, 'yellow': (T_CLOCK, T_CLOCK)}}



# maps the side cross pieces to the correct algorithm that will translate them to the bottom
side_cross = {'front': {2: (F_RIGHT, R_TOWARDS, BM_LEFT, R_AWAY), 4: (L_TOWARDS, BM_RIGHT, L_AWAY),
                        6: (R_TOWARDS, BM_LEFT, R_AWAY), 8: (F_RIGHT, L_TOWARDS, BM_LEFT, L_AWAY, F_LEFT)},
              'back': {2: (BA_RIGHT, R_AWAY, BM_LEFT, R_TOWARDS), 4: (R_AWAY, BM_LEFT, R_TOWARDS),
                       6: (L_AWAY, BM_RIGHT, L_TOWARDS), 8: (BA_LEFT, R_AWAY, BM_LEFT, R_TOWARDS, BA_RIGHT)},
              'left': {2: (L_TOWARDS, F_LEFT, BM_LEFT, F_RIGHT), 4: (BA_LEFT, BM_RIGHT, BA_RIGHT),
                       6: (F_LEFT, BM_LEFT, F_RIGHT), 8: (L_AWAY, F_LEFT, BM_RIGHT, F_RIGHT, L_TOWARDS)},
              'right': {2: (R_TOWARDS, F_RIGHT, BM_RIGHT, F_LEFT), 4: (F_RIGHT, BM_RIGHT, F_LEFT),
                       6: (BA_RIGHT, BM_LEFT, BA_LEFT), 8: (R_AWAY, F_RIGHT, BM_LEFT, F_LEFT, R_TOWARDS)}}



#===============================================================================
# # translates each corner piece to the 789 row of that face of the rubik's cube
# corner_to_789 = {'front': {}}
#===============================================================================



class RubixCube:
    
    def __init__(self, cube_config: dict):
        '''Initialize the Rubik's cube to contain the current configuration of the cube'''
        self.cube_config = cube_config
        self.steps = []
    
    def SolveTop(self) -> dict:
        cross_solved = False
        corners_solved = False
        
        def map_pieces(cube: dict) -> dict:
            '''map the cross pieces and return a dict of cross pieces mapped to adjacent pieces'''
            crosses = {}
            for face in cube:
                for position in cross:
                    if cube[face][position] == 'blue':
                        adj = cross_adjacents[face][position]
                        crosses[(face, position)] = adj + (cube[adj[0]][adj[1]],)
            return crosses
        
        def check_bottom(map: dict) -> dict:
            '''get all the blue pieces on the top or bottom to the correct place'''
            for current in map:
                if current[0] == 'bottom':
                    pass
        current_map = map_pieces(self.cube_config)
        print(current_map)        
        #=======================================================================
        # while cross_solved == False:
        #     current_map = map_pieces(self.cube_config)
        #     try:
        #         assert not (self.cube_config['top'][2] == 'blue' and self.cube_config['top'][4] == 'blue' and
        #                     self.cube_config['top'][6] == 'blue' and self.cube_config['top'][8] == 'blue' and
        #                     self.cube_config['front'][2] == 'white' and self.cube_config['right'][2] == 'red' and
        #                     self.cube_config['back'][2] == 'yellow' and self.cube_config['left'][2] == 'orange') 
        #     except AssertionError:
        #         cross_solved = True
        #=======================================================================
            
    
    def SolveMiddle(self) -> dict:
        pass
    
    def SolveCube(self) -> dict:
        pass
    
    def CheckCube(self) -> bool:
        sides_complete = 0
        for side in self.cube_config:
            if len(set(self.cube_config[side].values())) == 1:
                sides_complete += 1
        return True if sides_complete == 6 else False
    
    
    
 
#cube = RubixCube(cube).SolveTop()
#print('CUBE: ', cube)
#cube1 = eval('Moves(cube).R_AWAY()')
#print(cube1)
RubixCube(cube).SolveTop()

