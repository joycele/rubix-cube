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


# maps a direction to the complementary direction
complement = {'BM_LEFT': 'BM_RIGHT', 'BM_RIGHT': 'BM_LEFT', 'F_RIGHT': 'F_LEFT', 'F_LEFT': 'F_RIGHT',
             'BA_LEFT': 'BA_RIGHT', 'BA_RIGHT': 'BA_LEFT', 'L_AWAY': 'L_TOWARDS', 'L_TOWARDS': 'L_AWAY',
             'R_AWAY': 'R_TOWARDS', 'R_TOWARDS': 'R_AWAY', 'T_CLOCK': 'T_COUNTER_CLOCK', 'T_COUNTER_CLOCK': 'T_CLOCK',
             'ROTATE_CLOCK': 'ROTATE_COUNTER', 'ROTATE_COUNTER': 'ROTATE_CLOCK'}


# tuples indicating the cross and corner indices of the cube
cross = (2,4,6,8)
corner = (1,3,7,9)



cube = {'front': {1: 'white', 2: 'white', 3: 'white', 4: 'white', 5: 'white', 6: 'white', 7: 'white', 8: 'green', 9: 'yellow'},
        'left': {1: 'orange', 2: 'orange', 3: 'orange', 4: 'orange', 5: 'orange', 6: 'orange', 7: 'green', 8: 'green', 9: 'orange'}, 
        'right': {1: 'red', 2: 'red', 3: 'red', 4: 'red', 5: 'red', 6: 'red', 7: 'green', 8: 'green', 9: 'red'},
        'top': {1: 'blue', 2: 'blue', 3: 'blue', 4: 'blue', 5: 'blue', 6: 'blue', 7: 'blue', 8: 'blue', 9: 'blue'},
        'back': {1: 'yellow', 2: 'yellow', 3: 'yellow', 4: 'yellow', 5: 'yellow', 6: 'yellow', 7: 'green', 8: 'green', 9: 'orange'},
        'bottom': {1: 'green', 2: 'yellow', 3: 'red', 4: 'white', 5: 'green', 6: 'orange', 7: 'yellow', 8: 'red', 9: 'white'}}



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


# checks whether the side cross piece can be moved to the top instead of to the bottom
side_check = {'front': {4: {'orange': L_AWAY, 'red': False, 'yellow': False, 'white': False},
                        6: {'orange': False, 'red': R_AWAY, 'yellow': False, 'white': False}}, 
              'back': {4: {'orange': False, 'red': R_TOWARDS, 'yellow': False, 'white': False}, 
                       6: {'orange': L_TOWARDS, 'red': False, 'yellow': False, 'white': False}}, 
              'left': {4: {'orange': False, 'red': False, 'yellow': BA_RIGHT, 'white': False}, 
                       6: {'orange': False, 'red': False, 'yellow': False, 'white': F_RIGHT}}, 
              'right': {4: {'orange': False, 'red': False, 'yellow': False, 'white': F_LEFT}, 
                        6: {'orange': False, 'red': False, 'yellow': BA_LEFT, 'white': False}}}


# maps the correctly placed bottom corner pieces to the algorithm that will translate it to the top
corners_79 = {'front': {7: (BM_RIGHT, L_TOWARDS, BM_LEFT, L_AWAY), 9: (BM_LEFT, R_TOWARDS, BM_RIGHT, R_AWAY)}, 
              'right': {7: (BM_RIGHT, F_RIGHT, BM_LEFT, F_LEFT), 9: (BM_LEFT, BA_RIGHT, BM_RIGHT, BA_LEFT)},
              'left': {7: (BM_RIGHT, BA_LEFT, BM_LEFT, BA_RIGHT), 9: (BM_LEFT, F_LEFT, BM_RIGHT, F_RIGHT)},
              'back': {7: (BM_RIGHT, R_AWAY, BM_LEFT, R_TOWARDS), 9: (BM_LEFT, L_AWAY, BM_RIGHT, L_TOWARDS)}}


# maps corner pieces from the sides or bottom to the algorithm that will translate them to spots 7 or 9
to_bottom_row = {'front': {1: (L_TOWARDS, BM_LEFT, L_AWAY), 3: (R_TOWARDS, BM_RIGHT, R_AWAY)},
                 'right': {1: (F_RIGHT, BM_LEFT, F_LEFT), 3: (BA_RIGHT, BM_RIGHT, BA_LEFT)},
                 'left': {1: (BA_LEFT, BM_LEFT, BA_RIGHT), 3: (F_LEFT, BM_RIGHT, F_RIGHT)},
                 'back': {1: (R_AWAY, BM_LEFT, R_TOWARDS), 3: (L_AWAY, BM_RIGHT, L_TOWARDS)},
                 'bottom': {1: (L_TOWARDS, BM_LEFT, L_AWAY), 3: (R_TOWARDS, BM_RIGHT, R_AWAY),
                            7: (L_AWAY, BM_RIGHT, L_TOWARDS), 9: (R_AWAY, BM_LEFT, R_TOWARDS)}}


# maps a bottom piece to the correct corresponding top piece 
bottom_ok = {1: {('front', 1): 'white', ('left', 3): 'orange'}, 3: {('front', 3): 'white', ('right', 1): 'red'},
             7: {('left', 1): 'orange', ('back', 3): 'yellow'}, 9: {('right', 3): 'red', ('back', 1): 'yellow'}}


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


# left and right algorithms for moving the middle pieces into the correct place
middle_move = {'left': (T_COUNTER_CLOCK, L_AWAY, T_CLOCK, L_TOWARDS, T_CLOCK, F_RIGHT, T_COUNTER_CLOCK, F_LEFT),
               'right': (T_CLOCK, R_AWAY, T_COUNTER_CLOCK, R_TOWARDS, T_COUNTER_CLOCK, F_LEFT, T_CLOCK, F_RIGHT)}


# rotate top to get the top row middle piece in place
rotate_top = {2: {'back': True, 'right': T_CLOCK, 'left': T_COUNTER_CLOCK, 'front': (T_CLOCK, T_CLOCK)},
              4: {'back': T_CLOCK, 'right': (T_CLOCK, T_CLOCK), 'left': True, 'front': T_COUNTER_CLOCK},
              6: {'back': T_COUNTER_CLOCK, 'right': True, 'left': (T_CLOCK, T_CLOCK), 'front': T_CLOCK},
              8: {'back': (T_CLOCK, T_CLOCK), 'right': T_COUNTER_CLOCK, 'left': T_CLOCK, 'front': True}}


# maps the adjacent piece of every cross piece on each side
cross_adjacents = {'top': {2: ('back', 2), 4: ('left', 2), 6: ('right', 2), 8: ('front', 2)},
                   'front': {2: ('top', 8), 4: ('left', 6), 6: ('right', 4), 8: ('bottom', 2)},
                   'back': {2: ('top', 2), 4: ('right', 6), 6: ('left', 4), 8: ('bottom', 8)},
                   'bottom': {2: ('front', 8), 4: ('left', 8), 6: ('right', 8), 8: ('back', 8)},
                   'left': {2: ('top', 4), 4: ('back', 6), 6: ('front', 4), 8: ('bottom', 4)},
                   'right': {2: ('top', 6), 4: ('front', 6), 6: ('back', 4), 8: ('bottom', 6)}}


# solve the middle piece depending on which color it is
solve_piece = {'white': {'orange': middle_move['right'], 'red': middle_move['left']},
               'red': {'white': middle_move['right'], 'yellow': middle_move['left']},
               'orange': {'yellow': middle_move['right'], 'white': middle_move['left']},
               'yellow': {'red': middle_move['right'], 'orange': middle_move['left']}}


# maps the current front face of the cube to the algorithm that will rotate the cube to the desired front face
rotate_cube = {'white': {'orange': ROTATE_CLOCK, 'red': ROTATE_COUNTER, 'yellow': (ROTATE_CLOCK, ROTATE_CLOCK), 'white': True},
               'red': {'orange': (ROTATE_CLOCK, ROTATE_CLOCK), 'red': True, 'yellow': ROTATE_COUNTER, 'white': ROTATE_CLOCK},
               'orange': {'orange': True, 'red': (ROTATE_CLOCK, ROTATE_CLOCK), 'yellow': ROTATE_CLOCK, 'white': ROTATE_COUNTER},
               'yellow': {'orange': ROTATE_COUNTER, 'red': ROTATE_CLOCK, 'yellow': True, 'white': (ROTATE_CLOCK, ROTATE_CLOCK)}}


# algorithms used after middle portion is solved
dot_line = (F_RIGHT, R_AWAY, T_CLOCK, R_TOWARDS, T_COUNTER_CLOCK, F_LEFT)
L_shape = (F_RIGHT, R_AWAY, T_CLOCK, R_TOWARDS, T_COUNTER_CLOCK, R_AWAY, T_CLOCK, R_TOWARDS, T_COUNTER_CLOCK, F_LEFT)
align_cross = (R_AWAY, T_CLOCK, R_TOWARDS, T_CLOCK, R_AWAY, T_CLOCK, T_CLOCK, R_TOWARDS, T_CLOCK)
align_corners = (T_CLOCK, R_AWAY, T_COUNTER_CLOCK, L_AWAY, T_CLOCK, R_TOWARDS, T_COUNTER_CLOCK, L_TOWARDS)
solve_corners = (R_TOWARDS, BM_LEFT, R_AWAY, BM_RIGHT)


# rotate the cube according to how the top green pieces are positioned
L_config = {(2,4): True, (2,6): ROTATE_COUNTER, (4,8): ROTATE_CLOCK, (6,8): (ROTATE_CLOCK, ROTATE_CLOCK), (2,8): ROTATE_CLOCK}


# used for when a tuple needs to be used as a dictionary key
def translate(adj: tuple) -> tuple:
    '''Standardizes the the dictionary keys for rotate_bottom'''
    valid = [('orange', 'white'), ('red', 'white'), ('red', 'yellow'), ('orange', 'yellow')]
    for x in valid:
        if x == adj or (x[1], x[0]) == adj:
            return x 
        

class RubixCube:
     
    def __init__(self, cube_config: dict):
        '''Initialize the Rubik's cube to contain the current configuration of the cube'''
        self.cube_config = cube_config
        self.top_steps = []
        self.middle_steps = []
        self.cross_steps = []
        self.finish_steps = []
         
        self.cross_solved = (self.cube_config['top'][2] == 'blue' and self.cube_config['top'][4] == 'blue' and
                             self.cube_config['top'][6] == 'blue' and self.cube_config['top'][8] == 'blue' and
                             self.cube_config['front'][2] == 'white' and self.cube_config['right'][2] == 'red' and
                             self.cube_config['back'][2] == 'yellow' and self.cube_config['left'][2] == 'orange')
             
        self.corners_solved = (self.cube_config['top'][1] == 'blue' and self.cube_config['top'][3] == 'blue' and
                               self.cube_config['top'][7] == 'blue' and self.cube_config['top'][9] == 'blue' and 
                               self.cube_config['left'][1] == 'orange' and self.cube_config['back'][3] == 'yellow' and
                               self.cube_config['right'][3] == 'red' and self.cube_config['back'][1] == 'yellow' and
                               self.cube_config['left'][3] == 'orange' and self.cube_config['front'][1] == 'white' and
                               self.cube_config['right'][1] == 'red' and self.cube_config['front'][3] == 'white')
        
    def SolveTop(self) -> dict:
        '''Solves the top part of the Rubik's cube and returns the updated cube'''
         
        def map_blues(piece_type: tuple) -> dict or list:
            '''Map the blue pieces and return a dict of cross pieces mapped to adjacent pieces or a list of corner pieces
               tupled with their corresponding positions on the cube'''
            piece_dict = {}   # dict for returning cross pieces
            piece_list = []   # list for returning corner pieces
            for face in self.cube_config: 
                for position in piece_type:
                    if self.cube_config[face][position] == 'blue':   # find where all the blue's are positioned on the cube
                        if piece_type == cross:     # if it's a cross piece, add it to piece_dict mapped to its adjacent side
                            adj = cross_adjacents[face][position]
                            piece_dict[(face, position)] = self.cube_config[adj[0]][adj[1]]
                        if piece_type == corner:    # if it's a corner piece, append its face and position to the piece_list
                            piece_list.append((face, position))
            return piece_dict if piece_type == cross else piece_list   # return the list or dict according to the piece type
              
        def initial_top(top_map: [()]) -> list:
            '''Takes a list of tuples filtered to contain only top cross pieces and returns a list of algorithms to move them'''
            if len(top_map) == 4 or len(top_map) == 3:     # if there's 3 or 4 blue cross pieces on top, move them to the bottom
                for each in top_map:
                    if top_cross[each[0][1]][each[1]] != True:
                        algorithm = top_cross['move'][each[0][1]]
                        self.top_steps.append(algorithm)
            if len(top_map) == 2:     # if there's 2 blue cross pieces on top, find out which ones are in the correct position
                true_list = [top_cross[top_map[0][0][1]][top_map[0][1]], top_cross[top_map[1][0][1]][top_map[1][1]]]
                if True not in true_list:    # if none are in the correct position, move one down and rotate the other one
                    algorithm1 = top_cross['move'][top_map[0][0][1]]
                    algorithm2 = top_cross[top_map[1][0][1]][top_map[1][1]]
                    self.top_steps.extend([algorithm1, algorithm2])
                else:     # if one or both are in the correct position, take the appropriate algorithms
                    true_list.remove(True)
                    if len(true_list) == 1:
                        self.top_steps.append(true_list[0])
            if len(top_map) == 1:  # if there's only one cross piece on top, rotate it to the correct spot 
                algorithm = top_cross[top_map[0][0][1]][top_map[0][1]]
                if algorithm != True:   # if it's already in the correct spot, do nothing
                    self.top_steps.append(algorithm) 
         
        def solve_bottom() -> None:
            '''Solves any cross piece found on the bottom of the Rubik's cube'''
            while True:
                bottom_pieces = list(filter(lambda t: t[0][0] == 'bottom', list(map_blues(cross).items())))
                if len(bottom_pieces) == 0:
                    break     # if there's no bottom cross piece, break out of the loop
                algorithm = bottom_cross[bottom_pieces[0][0][1]][bottom_pieces[0][1]]
                self._execute(algorithm, self.top_steps)     # find the cross pieces and execute the algorithms
         
        def solve_side_crosses() -> None:
            '''Solves any cross pieces found on the right, left, front, or back sides of the cube'''
            while True:
                remaining_pieces = list(filter(lambda t: t[0][0] not in ('top', 'bottom'), list(map_blues(cross).items())))
                if len(remaining_pieces) == 0: 
                    break   # if there aren't any side cross pieces, break out of the loop
                side_pieces = list(filter(lambda t: t[0][1] in (4,6), remaining_pieces))
                good_sides = list(filter(lambda t: side_check[t[0][0]][t[0][1]][t[1]] != False, side_pieces))
                # find the good side pieces that are already in the right place
                if len(good_sides) != 0:   # if none of the side cross pieces are in the right place, rotate them to the bottom
                    for piece in good_sides:
                        algorithm = side_check[piece[0][0]][piece[0][1]][piece[1]]
                        self._execute(algorithm, self.top_steps)
                else:   # rotate the good side pieces to the top
                    algorithm = side_cross[remaining_pieces[0][0][0]][remaining_pieces[0][0][1]]
                    self._execute(algorithm, self.top_steps) 
                    solve_bottom()   # solve any cross piece found on the bottom of the cube
         
        def check_corners() -> bool or list:
            '''Checks whether the corner pieces are solved and returns True or a list of top pieces in the wrong place'''
            correct = 0   # indicates how many corner pieces are in the correct place
            incorrect = []   # contains a list of incorrectly placed top corner pieces
            corner_map = map_blues(corner) 
            for each in corner_map:
                if each[0] == 'top':   # find all the top corner pieces
                    current = list(top_correct[each[1]].items())
                    if (self.cube_config[current[0][0][0]][current[0][0][1]] == current[0][1] and 
                        self.cube_config[current[1][0][0]][current[1][0][1]] == current[1][1]):
                        correct += 1    # add 1 to correct if a corner piece is in the right place
                    else:
                        incorrect.append(each)   # append it to the incorrect list otherwise
            return True if correct == 4 else incorrect   # return True if all are in the right place or return the incorrect list
      
        def solve_corners() -> None:
            '''Solves the blue corner pieces'''
            check = check_corners()  
            if check == True:   # if every corner is already in the right place, do nothing
                return
            if len(check) == 4:  # if there are 4 incorrectly placed corner pieces on top, move one of them down
                algorithm = move_top[check[0][1]]
                self._execute(algorithm, self.top_steps)
            while check_corners() != True:  
                corner_map = list(filter(lambda t: t[0] != 'top', map_blues(corner)))  # map out the corner pieces not found on top
                if corner_map == []:   # if none are found, move one of the incorrect top pieces down
                    random_top = check_corners()[0]
                    algorithm = move_top[random_top[1]]
                    self._execute(algorithm, self.top_steps)
                else:   # find the corner pieces located on the bottom row in positions 7 or 9
                    bottom_row = list(filter(lambda t: t[0] != 'bottom' and t[1] in (7,9), corner_map))
                    if bottom_row == []:   # if none exist, move a piece to one of those positions
                        piece = corner_map[0]
                        if piece[0] == 'bottom':  # for the bottom pieces, check whether it is okay to move them
                            check = list(bottom_ok[piece[1]].items())
                            if (self.cube_config[check[0][0][0]][check[0][0][1]] == check[0][1] and
                                self.cube_config[check[1][0][0]][check[1][0][1]] == check[1][1]):
                                self._execute(BM_RIGHT, self.top_steps)  # if it isn't, move them to the right first
                            else:   # if it is, execute the algorithms needed to move them
                                algorithm = to_bottom_row[piece[0]][piece[1]]
                                self._execute(algorithm, self.top_steps)
                        else:   # for any piece not on the bottom, execute the algorithms needed to move them
                            algorithm = to_bottom_row[piece[0]][piece[1]]
                            self._execute(algorithm, self.top_steps)
                    else:    # if bottom row pieces are found in positions 7 or 9
                        adj = corner_adj[bottom_row[0][0]][bottom_row[0][1]]
                        adj_colors = self.cube_config[adj[0]][adj[1]], self.cube_config[adj[2]][adj[3]]
                        spot = rotate_bottom[bottom_row[0][0]][bottom_row[0][1]][translate(adj_colors)]
                        if spot == True:    # if the piece is already in the right place, solve the piece
                            algorithm = corners_79[bottom_row[0][0]][bottom_row[0][1]]
                            self._execute(algorithm, self.top_steps)
                        else:    # if the piece isn't in the right place, rotate the bottom row
                            self._execute(spot, self.top_steps)
        
        # put all the functions defined above together to solve the top part of the cube
        if self.cross_solved + self.corners_solved != 2:
            # if both cross and corners are already solved, return the cube
            if self.cross_solved:
                # if the cross is already solved, solve the corners
                solve_corners()
            else:
                # if neither cross nor corners are solved, solve for both
                cross_map = list(map_blues(cross).items())
                initial_top(list(filter(lambda t: t[0][0] == 'top', cross_map)))
                for algorithm in self.top_steps:
                    self._eval_step(algorithm)   # fix the initial top before preceding with solving the top and corners
                # move the side cross to the top or bottom, solve the bottom crosses, then solve for the corners
                solve_side_crosses()
                solve_bottom()
                solve_corners()
        return self.cube_config
             
     
    def SolveMiddle(self) -> dict:
        '''After the top part of the cube is solved, flip the cube upside down and solve the middle part'''
        assert self.cross_solved and self.corners_solved, 'Top failed to solve'
        self._execute(FLIP, self.middle_steps)  # flip cube
        
        # find all the middle pieces and their locations first before doing anything
        def find_all() -> list:
            '''Find all the middle pieces'''
            result = {}
            for face in ('right', 'left', 'front', 'back'):
                for position in (2,4,6):   # find side piece in positions 2, 4, and 6
                    if self.cube_config[face][position] != 'blue':
                        adj = cross_adjacents[face][position]
                        result[(face, position, self.cube_config[face][position])] = self.cube_config[adj[0]][adj[1]]
            # filter the pieces found so that none of them contain any green (top) pieces
            no_greens = list(filter(lambda t: t[0][2] != 'green' and t[1] != 'green', result.items()))
            return no_greens
        
        def get_config(color: str) -> dict:
            '''Get the face of the Rubik's cube depending on the given color'''
            for face in self.cube_config:
                if self.cube_config[face][5] == color:
                    return face
                
        def middle_solved() -> bool:
            '''Determines whether or not the middle part of the cube is solved'''
            try:
                for face in ('front', 'back', 'right', 'left'):
                    for position in (4,6):
                        assert self.cube_config[face][position] == self.cube_config[face][5]
                return True
            except AssertionError:
                return False
       
        while not middle_solved():
            middle_pieces = find_all()   # find all the middle pieces
            top_pieces = list(filter(lambda t: t[0][1] == 2, middle_pieces))  # filter the middle pieces to get only the top pieces
            if top_pieces == []:     # if there aren't any top pieces, take the appropriate algorithms
                if (self.cube_config['front'][4] != self.cube_config['front'][5] and 
                    self.cube_config['left'][6] != self.cube_config['left'][5]):
                    algorithm = middle_move['left'][1:]
                    self._execute(algorithm, self.middle_steps)
                elif (self.cube_config['front'][6] != self.cube_config['front'][5] and
                      self.cube_config['right'][4] != self.cube_config['right'][5]):
                    algorithm = middle_move['right'][1:]
                    self._execute(algorithm, self.middle_steps)
                else:   # keep rotating the cube until you find a middle piece in the incorrect place
                    while True:
                        self._execute(ROTATE_COUNTER, self.middle_steps)
                        if (self.cube_config['front'][4] != self.cube_config['front'][5] and
                            self.cube_config['left'][6] != self.cube_config['left'][5]):
                            break
                    algorithm = middle_move['left'][1:]   # move that middle piece to the top
                    self._execute(algorithm, self.middle_steps)
            else:    # if there are top pieces, filter them to find the ones already in the correct place
                correct_piece = list(filter(lambda t: t[0][2] == self.cube_config[t[0][0]][5], top_pieces))
                if correct_piece == []:    # if none of the top pieces are in the correct place, take the appropriate algorithms
                    top_piece = top_pieces[0]
                    adj = cross_adjacents[top_piece[0][0]][top_piece[0][1]]  
                    algorithm = rotate_top[adj[1]][get_config(top_piece[0][2])]
                    self._execute(algorithm, self.middle_steps) 
                else:    # if a top piece is in the correct place, see if any top piece is in front
                    correct_front = list(filter(lambda t: t[0][0] == 'front', correct_piece))
                    if correct_front == []:   # if there aren't any front pieces, rotate the cube and solve the piece
                        piece = correct_piece[0]
                        new_front = piece[0][2]
                        rotate_alg = rotate_cube[self.cube_config['front'][5]][new_front]
                        self._execute(rotate_alg, self.middle_steps) 
                    else:    # take the appropriate algorithms to solve the front piece
                        piece = correct_front[0]
                        algorithm = solve_piece[piece[0][2]][piece[1]]
                        self._execute(algorithm, self.middle_steps) 
        return self.cube_config
                    
                    
    def SolveTopCross(self) -> dict:
        '''Solve for the green cross on top'''   
        def cross_solved() -> bool:
            try:
                for i in cross:
                    assert self.cube_config['top'][i] == 'green'
                return True
            except AssertionError:
                return False
   
        def map_greens() -> list:
            '''Map all the positions of the green pieces at the top of the cube'''
            return [position for position in cross if self.cube_config['top'][position] == 'green']
            
        def solve_L(positions: list) -> None:
            '''Solve the green L shape'''
            if L_config[positions] == True:   # if L is in place, call algorithms without rotating cube
                self._execute(L_shape, self.cross_steps)
            else:    # otherwise, rotate the cube before properly solving the L
                self._execute(L_config[positions], self.cross_steps)  
                self._execute(L_shape, self.cross_steps) 
                
        def get_cross(positions: tuple) -> None:
            if positions == ():   # if there is just a green dot in the center, call an algorithm before solving the L
                self._execute(dot_line, self.cross_steps)
                new_positions = tuple(sorted(map_greens()))
                solve_L(new_positions)
            if positions in L_config:   # otherwise, solve the L normally
                solve_L(positions)
                
        if cross_solved():   # if the cross is already solved, return the cube
            return self.cube_config
        top_map = tuple(sorted(map_greens())) # get a map of the green cross pieces
        if top_map != cross:
            get_cross(top_map)
        if not cross_solved():   # if the cross still isn't solved, the cube wasn't configured/built properly
            raise InvalidCubeError('Cube configuration is invalid, unable to solve cube')
        return self.cube_config   
            
        
    def SolveRest(self) -> dict:
        '''Solve the remaining portion of the cube'''
        pass
        
     
    def CheckCube(self) -> bool:
        '''Checks whether the cube is solved'''
        sides_complete = 0
        for side in self.cube_config:
            if len(set(self.cube_config[side].values())) == 1:
                sides_complete += 1
        return True if sides_complete == 6 else False
     
    def _execute(self, alg: tuple or str, steps: list) -> None:
        '''Appends the algorithm to the list of steps and executes it'''
        if type(alg) == tuple:
            for each in alg:
                steps.append(each)
                eval(each)
        else:
            steps.append(alg)
            eval(alg)
            
    def _redundancy_two(self, l: list) -> None:
        '''Gets rid of redundant complementary algorithms'''
        count = None
        while count != 0:
            count = 0
            for i in range(len(l)):
                if i == len(l) - 1:
                    break
                if l[i][24:-2] == complement[l[i + 1][24:-2]]:
                    count += 1
                    del l[i:i+2]
                    break
    
    def _redundancy_four(self, l: list) -> None:
        '''Gets rid of algorithms that appear four times in a row'''
        count = None
        while count != 0:
            count = 0
        for i in range(len(l)):
            if i == len(l) - 1:
                break
            if l[i] == l[i + 1] == l[i + 2] == l[i + 3]:
                count += 1
                del l[i:i+4]
                break
    
    def _redundancy_three(self, l: list) -> None:
        '''Simplifies algorithms that appear three times in a row'''
        count = None
        while count != 0:
            count = 0
        for i in range(len(l)):
            if i == len(l) - 1:
                break
            if l[i] == l[i + 1] == l[i + 2]:
                count += 1
                replacement = complement[l[i][24:-2]]
                del l[i:i+3]
                self.top_steps.insert(i, 'Moves(self.cube_config).' + replacement + '()')
                break
            
    def _simplify(self, l: list) -> list:
        '''Combines all three redundancy check to simplify the overall list of algorithms'''
        self._redundancy_four(l)
        self._redundancy_two(l)
        self._redundancy_three(l)
        return l
 
    def _return_steps(self, step: str) -> list:
        '''Returns the list of the algorithms that was used to solve the specified step'''
        if step == 'top':
            return self.top_steps
     

class InvalidCubeError(Exception):
    '''Raised when the cube is configured in an impossible way'''
    pass
  
RubixCube(cube).SolveTop()
RubixCube(cube).SolveMiddle()
RubixCube(cube).SolveTopCross()





