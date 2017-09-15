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
corner = (1,3,7,9)



cube = {'front': {1: 'red', 2: 'yellow', 3: 'yellow', 4: 'blue', 5: 'white', 6: 'white', 7: 'white', 8: 'white', 9: 'red'}, 
        'top': {1: 'blue', 2: 'green', 3: 'yellow', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'white', 8: 'orange', 9: 'green'}, 
        'right': {1: 'orange', 2: 'orange', 3: 'blue', 4: 'green', 5: 'red', 6: 'white', 7: 'white', 8: 'yellow', 9: 'yellow'}, 
        'left': {1: 'green', 2: 'yellow', 3: 'red', 4: 'white', 5: 'orange', 6: 'red', 7: 'white', 8: 'green', 9: 'blue'}, 
        'back': {1: 'green', 2: 'yellow', 3: 'white', 4: 'red', 5: 'yellow', 6: 'orange', 7: 'orange', 8: 'orange', 9: 'orange'}, 
        'bottom': {1: 'orange', 2: 'green', 3: 'yellow', 4: 'red', 5: 'green', 6: 'red', 7: 'green', 8: 'green', 9: 'blue'}}



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



# either moves an incorrect top piece to the bottom, maps it to True, or moves an incorrect top piece to its correct place on top
top_cross = {2: {'red': T_CLOCK, 'orange': T_COUNTER_CLOCK, 'white': (T_CLOCK, T_CLOCK), 'yellow': True},
             4: {'red': (T_CLOCK, T_CLOCK), 'orange': True, 'white': T_COUNTER_CLOCK, 'yellow': T_CLOCK},
             6: {'red': True, 'orange': (T_CLOCK, T_CLOCK), 'white': T_CLOCK, 'yellow': T_COUNTER_CLOCK},
             8: {'red': T_COUNTER_CLOCK, 'orange': T_CLOCK, 'white': True, 'yellow': (T_CLOCK, T_CLOCK)},
             'move': {2: (BA_RIGHT, BA_RIGHT), 4: (L_TOWARDS, L_TOWARDS), 6: (R_TOWARDS, R_TOWARDS), 8: (F_RIGHT, F_RIGHT)}}



# maps the side cross pieces to the correct algorithm that will translate them to the bottom
side_cross = {'front': {2: (F_RIGHT, R_TOWARDS, BM_LEFT, R_AWAY), 4: (L_TOWARDS, BM_RIGHT, L_AWAY),
                        6: (R_TOWARDS, BM_LEFT, R_AWAY), 8: (F_RIGHT, L_TOWARDS, BM_LEFT, L_AWAY, F_LEFT)},
              'back': {2: (BA_RIGHT, R_AWAY, BM_LEFT, R_TOWARDS), 4: (R_AWAY, BM_LEFT, R_TOWARDS),
                       6: (L_AWAY, BM_RIGHT, L_TOWARDS), 8: (BA_LEFT, R_AWAY, BM_LEFT, R_TOWARDS, BA_RIGHT)},
              'left': {2: (L_TOWARDS, F_LEFT, BM_LEFT, F_RIGHT), 4: (BA_LEFT, BM_RIGHT, BA_RIGHT),
                       6: (F_LEFT, BM_LEFT, F_RIGHT), 8: (L_AWAY, F_LEFT, BM_RIGHT, F_RIGHT, L_TOWARDS)},
              'right': {2: (R_TOWARDS, F_RIGHT, BM_RIGHT, F_LEFT), 4: (F_RIGHT, BM_RIGHT, F_LEFT),
                       6: (BA_RIGHT, BM_LEFT, BA_LEFT), 8: (R_AWAY, F_RIGHT, BM_LEFT, F_LEFT, R_TOWARDS)}}



# maps the correctly placed bottom corner pieces to the algorithm that will translate it to the top
corners_79 = {'front': {7: (BM_RIGHT, L_TOWARDS, BM_LEFT, L_AWAY), 9: (BM_LEFT, R_TOWARDS, BM_RIGHT, R_AWAY)}, 
              'right': {7: (BM_RIGHT, F_RIGHT, BM_LEFT, F_LEFT), 9: (BM_LEFT, BA_RIGHT, BM_RIGHT, BA_LEFT)},
              'left': {7: (BM_RIGHT, BA_LEFT, BM_LEFT, BA_RIGHT), 9: (BM_LEFT, F_LEFT, BM_RIGHT, F_RIGHT)},
              'back': {7: (BM_RIGHT, R_AWAY, BM_LEFT, R_TOWARDS), 9: (BM_LEFT, L_AWAY, BM_RIGHT, L_TOWARDS)}}



# maps the top 1 and 3 positioned corner pieces to the algorithm that will translate them to spots 7 or 9
top_13 = {'front': {1: (L_TOWARDS, BM_LEFT, L_AWAY), 3: (R_TOWARDS, BM_RIGHT, R_AWAY)},
          'right': {1: (F_RIGHT, BM_LEFT, F_LEFT), 3: (BA_RIGHT, BM_RIGHT, BA_LEFT)},
          'left': {1: (BA_LEFT, BM_LEFT, BA_RIGHT), 3: (F_LEFT, BM_RIGHT, F_RIGHT)},
          'back': {1: (R_AWAY, BM_LEFT, R_TOWARDS), 3: (L_AWAY, BM_RIGHT, L_TOWARDS)}}



# maps the corner pieces on the bottom to corners 7 or 9 on the right/left/back/front sides
bottom_corners = {1: (L_TOWARDS, BM_LEFT, L_AWAY), 3: (R_TOWARDS, BM_RIGHT, R_AWAY), 
                  7: (L_AWAY, BM_RIGHT, L_TOWARDS), 9: (R_AWAY, BM_LEFT, R_TOWARDS)}



# maps the adjacent pieces of every blue bottom corner piece and all the top pieces
corner_adj = {'front': {7: ('left', 9, 'bottom', 1), 9: ('right', 7, 'bottom', 3)},
              'right': {7: ('front', 9, 'bottom', 3), 9: ('back', 7, 'bottom', 9)},
              'left': {7: ('back', 9, 'bottom', 7), 9: ('front', 7, 'bottom', 1)},
              'back': {7: ('right', 9, 'bottom', 9), 9: ('left', 7, 'bottom', 7)},
              'top': {1: ('back', 3, 'left', 1), 3: ('back', 1, 'right', 3), 
                      7: ('left', 3, 'front', 1), 9: ('right', 1, 'front', 3)}}



# algorithms to move incorrectly placed top corner pieces to a spot on the bottom
move_top = {1: (BA_LEFT, BM_RIGHT, BA_RIGHT), 3: (BA_RIGHT, BM_LEFT, BA_LEFT),
            7: (L_TOWARDS, BM_RIGHT, L_AWAY), 9: (R_TOWARDS, BM_LEFT, R_AWAY)}



# maps bottom pieces to the correct algorithm or to True if they are already in the right place
rotate_bottom = {'front': {7: {('orange', 'white'): True, ('red', 'white'): BM_RIGHT, 
                               ('red', 'yellow'): (BM_RIGHT, BM_RIGHT), ('orange', 'yellow'): BM_LEFT}, 
                           9: {('red', 'white'): True, ('orange', 'white'): BM_LEFT,
                               ('orange', 'yellow'): (BM_LEFT, BM_LEFT), ('red', 'yellow'): BM_RIGHT}}, 
                 'right': {7: {('orange', 'yellow'): (BM_RIGHT, BM_RIGHT), ('red', 'white'): True,
                               ('orange', 'white'): BM_LEFT, ('red', 'yellow'): BM_RIGHT}, 
                           9: {('red', 'white'): BM_LEFT, ('orange', 'white'): (BM_LEFT, BM_LEFT),
                               ('red', 'yellow'): True, ('orange', 'yellow'): BM_RIGHT}}, 
                 'left': {7: {('red', 'white'): (BM_RIGHT, BM_RIGHT), ('orange', 'white'): BM_RIGHT,
                              ('red', 'yellow'): BM_LEFT, ('orange', 'yellow'): True}, 
                          9: {('red', 'yellow'): (BM_RIGHT, BM_RIGHT), ('red', 'white'): BM_RIGHT,
                              ('orange', 'yellow'): BM_LEFT, ('orange', 'white'): True}}, 
                 'back': {7: {('orange', 'yellow'): BM_RIGHT, ('red', 'yellow'): True,
                              ('orange', 'white'): (BM_LEFT, BM_LEFT), ('red', 'white'): BM_LEFT}, 
                          9: {('red', 'white'): (BM_RIGHT, BM_RIGHT), ('red', 'yellow'): BM_LEFT,
                              ('orange', 'yellow'): True, ('orange', 'white'): BM_RIGHT}}}



# maps the top corner pieces to the correct adjacent pieces
top_correct = {1: {('back', 3): 'yellow', ('left', 1): 'orange'}, 3: {('back', 1): 'yellow', ('right', 3): 'red'},
               7: {('left', 3): 'orange', ('front', 1): 'white'}, 9: {('right', 1): 'red', ('front', 3): 'white'}}







class RubixCube:
    
    def __init__(self, cube_config: dict):
        '''Initialize the Rubik's cube to contain the current configuration of the cube'''
        self.cube_config = cube_config
        self.top_steps = []
    
    def SolveTop(self) -> dict:
        '''Solves the top part of the Rubik's cube and returns the updated cube'''
        
        cross_solved = (self.cube_config['top'][2] == 'blue' and self.cube_config['top'][4] == 'blue' and
                        self.cube_config['top'][6] == 'blue' and self.cube_config['top'][8] == 'blue' and
                        self.cube_config['front'][2] == 'white' and self.cube_config['right'][2] == 'red' and
                        self.cube_config['back'][2] == 'yellow' and self.cube_config['left'][2] == 'orange')
        
        corners_solved = (self.cube_config['top'][1] == 'blue' and self.cube_config['top'][3] == 'blue' and
                          self.cube_config['top'][7] == 'blue' and self.cube_config['top'][9] == 'blue' and 
                          self.cube_config['left'][1] == 'orange' and self.cube_config['back'][3] == 'yellow' and
                          self.cube_config['right'][3] == 'red' and self.cube_config['back'][1] == 'yellow' and
                          self.cube_config['left'][3] == 'orange' and self.cube_config['front'][1] == 'white' and
                          self.cube_config['right'][1] == 'red' and self.cube_config['front'][3] == 'white')
        
        def map_blues(piece_type: tuple) -> dict or list:
            '''Map the blue pieces and return a dict of cross pieces mapped to adjacent pieces or a list of corner pieces
               tupled with their corresponding positions on the cube'''
            piece_dict = {}
            piece_list = []
            for face in self.cube_config:
                for position in piece_type:
                    if self.cube_config[face][position] == 'blue':
                        if piece_type == cross:
                            adj = cross_adjacents[face][position]
                            piece_dict[(face, position)] = self.cube_config[adj[0]][adj[1]]
                        if piece_type == corner:
                            piece_list.append((face, position))
            return piece_dict if piece_type == cross else piece_list
             
        def initial_top(top_map: [()]) -> list:
            '''Takes a list of tuples filtered to contain only top cross pieces and returns a list of algorithms to move them'''
            if len(top_map) == 4 or len(top_map) == 3:
                for each in top_map:
                    if top_cross[each[0][1]][each[1]] != True:
                        algorithm = top_cross['move'][each[0][1]]
                        self.top_steps.append(algorithm)
            if len(top_map) == 2:
                true_list = [top_cross[top_map[0][0][1]][top_map[0][1]], top_cross[top_map[1][0][1]][top_map[1][1]]]
                if True not in true_list:
                    algorithm1 = top_cross['move'][top_map[0][0][1]]
                    algorithm2 = top_cross[top_map[1][0][1]][top_map[1][1]]
                    self.top_steps.extend([algorithm1, algorithm2])
                else:
                    true_list.remove(True)
                    if len(true_list) == 1:
                        self.top_steps.append(true_list[0])
            if len(top_map) == 1:
                algorithm = top_cross[top_map[0][0][1]][top_map[0][1]]
                self.top_steps.append(algorithm) 
        
        def solve_bottom() -> None:
            '''Solves any piece found on the bottom of the Rubik's cube'''
            while True:
                bottom_pieces = list(filter(lambda t: t[0][0] == 'bottom', list(map_blues(cross).items())))
                if len(bottom_pieces) == 0:
                    break
                algorithm = bottom_cross[bottom_pieces[0][0][1]][bottom_pieces[0][1]]
                self.top_steps.append(algorithm)
                self._eval_step(algorithm)
        
        def solve_side_crosses() -> None:
            '''Solves any cross pieces found on the right, left, front, or back sides of the cube'''
            while True:
                remaining_pieces = list(filter(lambda t: t[0][0] not in ('top', 'bottom'), list(map_blues(cross).items())))
                if len(remaining_pieces) == 0:
                    break
                algorithm = side_cross[remaining_pieces[0][0][0]][remaining_pieces[0][0][1]]
                self.top_steps.append(algorithm)
                self._eval_step(algorithm)
                solve_bottom()
        
        def solve_corners(corners: list) -> None:
            '''Solves the blue corner pieces'''
            print(corners)
        
        solve_corners(map_blues(corner))
            
        
        if cross_solved + corners_solved == 2:
            return self.cube_config
        else:
            if cross_solved:
                pass
            else:
                cross_map = list(map_blues(cross).items())
                initial_top(list(filter(lambda t: t[0][0] == 'top', cross_map)))
                for algorithm in self.top_steps:
                    self._eval_step(algorithm)
                solve_bottom()
                solve_side_crosses()
                print('total steps: ', self.top_steps)
                print('cube: ', self.cube_config)
            
    
    def SolveMiddle(self) -> dict:
        pass
    
    def SolveCube(self) -> dict:
        pass
    
    def CheckCube(self) -> bool:
        '''Checks whether the cube is solved'''
        sides_complete = 0
        for side in self.cube_config:
            if len(set(self.cube_config[side].values())) == 1:
                sides_complete += 1
        return True if sides_complete == 6 else False
    
    def _eval_step(self, step: tuple or str) -> None:
        '''Evaluates the algorithm given'''
        if type(step) == tuple:
            for each in step:
                eval(each)
        else:
            eval(step)
    
    def _return_steps(self, step: str) -> list:
        '''Returns the list of the algorithms that was used to solve the specified step'''
        if step == 'top':
            return self.top_steps
    
    
    
 
#cube = RubixCube(cube).SolveTop()
#print('CUBE: ', cube)
#cube1 = eval('Moves(cube).R_AWAY()')
#print(cube1)
RubixCube(cube).SolveTop()

